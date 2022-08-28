import logging
import uuid

from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser, ReferralItem
from apps.bot_users.serializers import CreateBotUserRequest, \
    UpdateBotUserRequest
from apps.bot_users.exceptions import BotUserNotFound


logger = logging.getLogger(__name__)


@api_view(['GET'])
def user_list_ids():
    user_ids = BotUser.objects.all().values('user_id')
    return Response(data=user_ids, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    return Response(data={
        'user_id': user.user_id
    })


@api_view(['POST'])
@transaction.atomic
def create_user(request):
    data = request.data
    CreateBotUserRequest(data=data).is_valid(True)

    referral_owner = None
    if data.get('referral_value', None):
        try:
            referral_owner = BotUser.objects.get(referral_value=data['referral_value'])
        except BotUser.DoesNotExist:
            raise BotUserNotFound

    referral_value = 'ref' + str(data['user_id'])[:-4] + str(uuid.uuid4())[:4]

    with transaction.atomic():
        new_user = BotUser.objects.create(
            user_id=data['user_id'],
            user_name=data['user_name'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            referral_value=referral_value
        )

        referral_id = None
        if referral_owner:
            referral_item = ReferralItem.objects.create(
                referral_owner_id=referral_owner.user_id,
                referred_user_id=new_user.user_id,
                is_activated_reward=False
            )

        logger.info(f'Add new user {new_user.user_id} with referral {referral_owner.user_id}' if referral_id else f'Add new user {new_user.user_id}')

        # result = serializers.serialize('json', [new_user, ])
        return Response({
            'user_id': new_user.user_id,
            'user_name': new_user.user_name,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'is_bot_blocked': new_user.is_bot_blocked,
            'referral_value': new_user.referral_value,
            'referral_item_id': referral_item.id
        }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@transaction.atomic
def update_user(request, user_id):
    logger.info(f'Update user {user_id}')

    data = request.data
    UpdateBotUserRequest(data=data).is_valid(True)

    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    with transaction.atomic():
        user.user_name = data['user_name']
        user.first_name = data['first_name']
        user.last_name = data['last_name']

        if not user.referral_item and data['referral_value']:
            try:
                referral_owner = BotUser.objects.get(referral_value=data['referral_value'])
            except BotUser.DoesNotExist:
                raise BotUserNotFound

            referral_id = ReferralItem.objects.create(
                referral_owner_id=referral_owner.user_id,
                referred_user_id=user.user_id,
                is_activated_reward=False
            )
            logger.info(f'Add referral {referral_id} of user {user_id}')

        user.save()

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_referral_data(request, user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    data = {
        'referral_link': f'https://t.me/{settings.BOT_USER_NAME}?start={user.referral_value}',
        'count_referrals': user.referrals_count,
        'count_free_month_subscription': user.free_referrals_count
    }

    return Response(data=data, status=status.HTTP_200_OK)