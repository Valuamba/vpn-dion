from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_device_tariff.serializers import VpnDeviceTariffSerializer


class VpnDeviceTariffViewSet(ModelViewSet):
    queryset = VpnDeviceTariff.objects.all()
    serializer_class = VpnDeviceTariffSerializer
