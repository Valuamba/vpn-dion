import ast
import decimal

from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, \
    PaymentDetailsResponseSerializer, CreateSubscriptionConfigsRequest, CreateSubscriptionSerilizer


@api_view(['POST'])
def create_subscription(request):
    data = request.data
    CreateSubscriptionSerilizer(data=data).is_valid(True)

    subscription = VpnSubscription.objects.create(
        user_id=data['user_id'],
        tariff_id=data['tariff_id'],
        status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT
    )

    for device in data['devices']:
        instances = VpnInstance.objects.filter(country__pkid=device['country_id'], protocols__pkid=device['protocol_id'], is_online=True)
        if len(instances) == 0:
            return Response(data={'detailed: There are no instances'}, status=status.HTTP_404_NOT_FOUND)

        VpnItem.objects.create(
            instance=instances[0],
            protocol_id=device['protocol_id'],
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

    sid = transaction.savepoint()
    subscription.status = SubscriptionPaymentStatus.PAID_SUCCESSFULLY
    subscription.save()

    vpn_items = subscription.vpn_items_list

    configs = []
    try:
        for item in vpn_items:
            client_response = item.instance.client.create_client(subscription.user.user_id)
            configs.append(client_response)
    except Exception as e:
        transaction.savepoint_rollback(sid)
        return Response(data={'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    transaction.savepoint_commit(sid)
    return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def calculate_payment_details(request):
#     data = request.data
#     serializer = CalculatePaymnetDataSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     payment_details = serializer.data
#
#     default_duration_price = VpnDurationPrice.objects.get(month_duration=1)
#     tariff = VpnDeviceTariff.objects.get(pkid=payment_details['duration_tariff_id'])
#
#     devices = payment_details['devices']
#
#     initial_price = tariff.devices_number * default_duration_price.amount * tariff.duration_data.month_duration
#
#     discount = decimal.Decimal((100 - tariff.discount_percentage) / 100)
#
#     duration_price = decimal.Decimal(0.0)
#     for i in range(tariff.devices_number):
#         device_amount = tariff.duration_data.amount
#         if i <= len(devices) - 1:
#             device = devices[i]
#             country = VpnCountry.objects.get(pkid=device['country_id'])
#             country_discount = decimal.Decimal((100 - country.discount_percentage) / 100)
#             device_amount = tariff.duration_data.amount * country_discount
#         duration_price += device_amount * tariff.duration_data.month_duration
#
#     discounted_price = duration_price * discount
#     discount_percentage = round(100 - ((discounted_price * 100) / initial_price))
#
#     response_serializer = PaymentDetailsResponseSerializer(data={
#         "initial_amount": round(initial_price, 2),
#         "discounted_amount": round(discounted_price, 2),
#         "discount_percentage": round(discount_percentage, 2)
#     })
#     response_serializer.is_valid(True)
#
#     return Response(data=response_serializer.data, status=status.HTTP_200_OK)

