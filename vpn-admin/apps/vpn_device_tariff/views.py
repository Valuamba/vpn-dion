import logging

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_device_tariff.serializers import CalculatePaymnetDataSerializer, \
    PaymentDetailsResponseSerializer
from lib.morph import get_morph


logger = logging.getLogger(__name__)

@api_view(['POST'])
def get_devices_result_payment_details(request):
    serializer = CalculatePaymnetDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    payment_details = serializer.data

    tariff = VpnDeviceTariff.objects.get(pkid=payment_details['duration_tariff_id'])

    response_serializer = PaymentDetailsResponseSerializer(data={
        "initial_amount": round(tariff.initial_price),
        "discounted_amount": round(tariff.discounted_price(payment_details['devices'])),
        "discount_percentage": round(tariff.discount_percentage)
        })
    response_serializer.is_valid(True)

    return Response(data=response_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tariffs_data(requests):
    logger.info(f'Get tariffs data.')
    tariffs = VpnDeviceTariff.objects.all()

    tariffs_data = []
    for tariff in tariffs:
        tariffs_data.append({
            'tariff_id': tariff.pkid,
            'month_duration': tariff.duration.month_duration,
            'month_loc': get_morph('месяц', tariff.duration.month_duration),
            'devices_number': tariff.devices_number,
            'devices_loc': get_morph('устройство', tariff.devices_number),
            'price': tariff.discounted_price(),
            'currency': "RUB",
            'discount': tariff.total_discount
        })

    return Response(data=tariffs_data, status=status.HTTP_200_OK)

