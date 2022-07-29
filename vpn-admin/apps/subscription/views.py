import decimal
from datetime import datetime, timezone
from typing import List

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import views
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.bot_assets.models import VpnSubscriptionOffer, VpnDurationPrice, VpnCountry, VpnProtocol
from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.subscription.models import VpnSubscription, Instance, VpnItem, SubscriptionPaymentStatus
from apps.subscription.serializers import VpnSubscriptionSerializer, InstanceSerializer, DeviceSerializer
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
        # currency=data["currency"],
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


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def calculate_total_price(request):
    data = request.data

    devices= data["devices"]
    month_duration = data["month_duration"]

    offers = VpnSubscriptionOffer.objects.filter()
    duration_price: VpnDurationPrice = VpnDurationPrice.objects.get(month_duration=month_duration)
    countries = VpnCountry.objects.filter()

    matched_offer = None
    for offer in offers:
        if offer.operation == VpnSubscriptionOffer.OperationType.EQUAL \
                and offer.month_duration == month_duration \
                and offer.devices_number == len(devices):
            matched_offer = offer
            break
        elif offer.operation == VpnSubscriptionOffer.OperationType.GREATER_THAN_OR_EQUAL \
                and offer.month_duration == month_duration \
                and  len(devices) >= offer.devices_number:
            matched_offer = offer
            break

    total_price = decimal.Decimal(0)
    total_discount = matched_offer.discount_percentage

    for device in devices:
        country = next(country for country in countries if device['country'] == country.country.name)
        total_price += duration_price.price.amount * (100 - country.discount_percentage) / 100

    return Response(data={
        'total_price': total_price,
        'total_discount': total_discount
    }, status=status.HTTP_200_OK)


class GetOnlineInstancesAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Instance.objects.filter(is_online=True)
    serializer_class = InstanceSerializer


@api_view(['POST'])
def create_subscription(request):
    data = request.data
    devices = data['devices']
    user_id = data['user_id']
    tariff_id = data['tariff_id']

    try:
        bot_user: BotUser = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    tariff = VpnSubscriptionOffer.objects.get(pkid=tariff_id)

    subscription = VpnSubscription.objects.create(
        user=bot_user,
        amount_of_devices=tariff.devices_number,
        amount_of_month=tariff.duration.month_duration,
        subscription_datetime_utc=datetime.now(timezone.utc),
        # currency=tariff.duration.price.currency,
        total_price=123,
        discount=12,
        status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT
    )

    if (tariff.operation == VpnSubscriptionOffer.OperationType.EQUAL and len(devices) != tariff.devices_number)\
            or (tariff.operation == VpnSubscriptionOffer.OperationType.GREATER_THAN_OR_EQUAL and len(devices) < tariff.devices_number):
        return Response({"details": "Count of devices doesn't equal to expected count."})

    for device in devices:
        instances = Instance.objects.filter(country__pkid=int(device['country_id']), protocols__pkid=int(device['protocol_id']), is_online=True)
        if len(instances) == 0:
            return Response({"details": 'There is no online instances'}, status=status.HTTP_403_FORBIDDEN)

        protocol = VpnProtocol.objects.get(pkid=int(device['protocol_id']))
        instance = instances[0]

        vpn_item = VpnItem.objects.create(
            instance=instance,
            protocol=protocol,
            vpn_subscription=subscription,
        )

    serializer = VpnSubscriptionSerializer(subscription, many=False)

    return Response(serializer.data['pkid'], status=status.HTTP_200_OK)


class CreateSubscription(views.APIView):

    def post(self, request, *args, **kwargs):

        device_serializer = DeviceSerializer(data=request.data['devices'][0])

        # device_serializer.is_valid()
        d = device_serializer.initial_data

        return super(CreateSubscription, self).post()

    # def create(self, request, *args, **kwargs):
    #     ''' I wanted to do some stuff with serializer.data here '''
    #     return super(CreateSubscription, self).create(request, *args, **kwargs)


