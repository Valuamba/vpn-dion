import ast
import decimal
import json
import logging
import traceback

from django.db import transaction
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, PaymentDetailsResponseSerializer, \
    CreateSubscriptionConfigsRequest, CreateSubscriptionSerilizer
from lib.vpn_server.datatypes import VpnConfig


logger = logging.getLogger(__name__)


@api_view(['POST'])
@transaction.atomic
def create_subscription(request):
    data = request.data
    CreateSubscriptionSerilizer(data=data).is_valid(True)

    with transaction.atomic():
        subscription = VpnSubscription.objects.create(user_id=data['user_id'], tariff_id=data['tariff_id'],
            status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT
        )

        for device in data['devices']:
            instances = VpnInstance.objects.filter(country__pkid=device['country_id'],
                                                   protocols__pkid=device['protocol_id'], is_online=True
                                                   )
            if len(instances) == 0:
                return Response(data={'detailed: There are no instances'}, status=status.HTTP_404_NOT_FOUND)

            VpnItem.objects.create(instance=instances[0], protocol_id=device['protocol_id'],
                vpn_subscription_id=subscription.pkid
            )

    return Response(data=subscription.pkid, status=status.HTTP_200_OK)


@api_view(['POST'])
@transaction.atomic
def config_files(request):
    data = request.data
    CreateSubscriptionConfigsRequest(data=data).is_valid(True)

    try:
        subscription = VpnSubscription.objects.get(pkid=data['subscription_id'])
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)

    if subscription.status != SubscriptionPaymentStatus.WAITING_FOR_PAYMENT:
        return Response(data={'details': 'Subscription has wrong status'}, status=status.HTTP_404_NOT_FOUND)

    changed_items = []
    try:
        with transaction.atomic():
            subscription.status = SubscriptionPaymentStatus.PAID_SUCCESSFULLY
            subscription.save()
            vpn_items = subscription.vpn_items_list

            for item in vpn_items:
                print ('Some')
                logger.info(f'Create config for vpn item {item.pkid}')
                client_response: VpnConfig = item.instance.client.create_client(subscription.user.user_id)
                item.public_key = client_response.public_key
                item.private_key = client_response.private_key
                item.address = client_response.address
                item.dns = client_response.dns
                item.preshared_key = client_response.preshared_key
                item.endpoint = client_response.endpoint
                item.allowed_ips = client_response.allowed_ips
                item.config_name = client_response.config_name
                item.save()
                changed_items.append(item)
    except Exception as e:
        for item in changed_items:
            item.instance.client.remove_client(item.config_name)
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic
def fail_subscription(request, subscription_id):
    try:
        subscription = VpnSubscription.objects.get(pkid=subscription_id)
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)
    subscription.status = SubscriptionPaymentStatus.PAYMENT_WAS_FAILED
    subscription.save()

    for item in subscription.vpn_items_list:
        item.instance.client.remove_client(item.config_name)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def list_user_subscriptions(request, user_id):
    try:
        subscriptions = VpnSubscription.objects.filter(user_id=user_id).values('user', 'tariff', )
    except VpnSubscription.DoesNotExist:
        return Response(data={'details': 'Subscription was not found'}, status=status.HTTP_404_NOT_FOUND)

    # return JsonResponse(list(subscriptions), safe=False)
    result = VpnSubscriptionSerializer(data=list(subscriptions), many=True)
    result.is_valid(True)

    return Response(data=result.data, status=status.HTTP_200_OK)

