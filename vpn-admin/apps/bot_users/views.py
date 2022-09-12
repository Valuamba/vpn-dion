import logging
import uuid

from django.conf import settings
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.bot_users.models import BotUser, ReferralItem
from apps.bot_users.serializers import CreateBotUserRequest, \
    UpdateBotUserRequest
from apps.bot.exceptions import BotUserNotFound


logger = logging.getLogger(__name__)


@api_view(['GET'])
def user_list_ids():
    logger.info('Get users list.')
    user_ids = BotUser.objects.all().values('user_id')
    return Response(data=user_ids, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_by_id(request, user_id):
    logger.info(f'Get user {user_id}')
    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    return Response(data={
        'user_id': user.user_id
    })


@api_view(['PUT'])
@transaction.atomic
def update_user(request, user_id):
    logger.info(f'Update user {user_id}')

    data = request.data
    UpdateBotUserRequest(data=data).is_valid(True)

    logger.info(f'Update user {user_id}')
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


