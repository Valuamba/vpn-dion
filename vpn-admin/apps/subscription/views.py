from datetime import datetime, timezone
from typing import List

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.subscription.models import VpnSubscription
from apps.subscription.serializers import VpnSubscriptionSerializer
from apps.vpn.models import VpnItem
from apps.vpn_instance.models import Instance
from lib.subscription_calculator import calculate_subscription_discount
from lib.vpn_server.datatypes import VpnConfig


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def create_vpn_item(request, user_id):
    try:
        bot_user: BotUser = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    data = request.data

    try:
        instance: Instance = Instance.objects.get(id=data["instance_id"])
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    amount_of_devices = data["amount_of_devices"]
    amount_of_month = data["amount_of_devices"]

    vpn_configs = []
    vpn_items: List[VpnItem] = []

    discount = calculate_subscription_discount(
        amount_of_devices=amount_of_devices,
        amount_of_month=amount_of_month
    )

    subscription = VpnSubscription.objects.create(
        user=bot_user,
        amount_of_devices=amount_of_devices,
        amount_of_month=amount_of_month,
        subscription_datetime_utc=datetime.now(timezone.utc),
        currency=data["currency"],
        total_price=data["total_price"],
        discount=discount
    )

    for i in range(amount_of_devices):
        vpn_response: VpnConfig = instance.client.create_client(bot_user.get_full_name(), amount_of_month)
        vpn_configs.append(vpn_response)

        vpn_item = VpnItem.objects.create(
            instance=instance,
            vpn_subscription=subscription,
            **vpn_response.__dict__
        )
        vpn_items.append(vpn_item)

    serializer = VpnSubscriptionSerializer(subscription, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

