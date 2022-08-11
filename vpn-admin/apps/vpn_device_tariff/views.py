from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_device_tariff.serializers import VpnDeviceTariffSerializer, CalculatePaymnetDataSerializer, \
    PaymentDetailsResponseSerializer


class VpnDeviceTariffViewSet(ModelViewSet):
    queryset = VpnDeviceTariff.objects.all().order_by('duration__month_duration', 'devices_number')
    serializer_class = VpnDeviceTariffSerializer


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

