from datetime import datetime, timezone
from typing import List

from django.db import transaction
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.subscription.models import VpnSubscription
from apps.vpn.models import VpnItem
from lib.subscription_calculator import calculate_subscription_discount
from lib.vpn_server_api_client import call_api


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def create_vpn_item(request, user_id):
    try:
        bot_user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    data = request.data

    amount_of_devices = data.amount_of_devices
    amount_of_month = data.amount_of_devices

    vpn_configs = []
    vpn_items: List[VpnItem] = []

    for i in range(amount_of_devices):
        vpn_response = call_api('localhost:57765', 'createConfig', data={
            'username': data.username,
            'amount_of_month': data.amount_of_month
        })

        vpn_content = vpn_response.content
        vpn_configs.append(vpn_content)

        vpn_item = VpnItem.objects.create(
            public_key=vpn_content.public_key,
            private_key=vpn_content.private_key,
            address=vpn_content.address,
            dns=vpn_content.dns,
            preshared_key=vpn_content.preshared_key,
            endpoint=vpn_content.endpoint,
            allowed_ips=vpn_content.allowed_ips,
            config_name=vpn_content.config_name
        )
        vpn_items.append(vpn_item)

    discount = calculate_subscription_discount(
        amount_of_devices=amount_of_devices,
        amount_of_month=amount_of_month
    )

    subscription = VpnSubscription.objects.create(
        user=bot_user,
        amount_of_devices=amount_of_devices,
        amount_of_month=amount_of_month,
        subscription_datetime_utc=datetime.now(timezone.utc),
        currency=data.currency,
        total_price=data.total_price,
        discount=discount
    )

