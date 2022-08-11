import ast
import decimal

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, \
    PaymentDetailsResponseSerializer


@api_view(['POST'])
def create_subscription(request):
    data = request.data
    vpn_items = [ast.literal_eval(item) for item in data.pop('vpn_items')]

    serializer = VpnSubscriptionSerializer(data)
    serializer.is_valid(True)
    serializer.save()

    new_vpn_items = []
    for vpn_item in vpn_items:
        new_vpn_item = VpnItemCreateSerializer().create({
            **vpn_item,
            'vpn_subscription_id': serializer.data.pkid
        }
        )
        new_vpn_items.append(new_vpn_item.id)

    return Response()


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

