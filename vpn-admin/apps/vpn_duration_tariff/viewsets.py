from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_duration_tariff.serializers import VpnDurationPriceSerializer


class VpnDurationPriceViewSet(ModelViewSet):
    queryset = VpnDurationPrice.objects.all()
    serializer_class = VpnDurationPriceSerializer