from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class VpnProtocolViewSet(ModelViewSet):
    queryset = VpnProtocol.objects.filter(instances__is_online=True)
    serializer_class = VpnProtocolSerializer