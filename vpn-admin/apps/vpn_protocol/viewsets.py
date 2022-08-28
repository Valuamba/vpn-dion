from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class VpnProtocolViewSet(ModelViewSet):
    queryset = VpnProtocol.objects.raw('''
SELECT p.pkid, p.protocol, p.is_default FROM public.vpn_protocols as p
INNER JOIN public.vpn_instances on country_id = p.pkid
GROUP BY p.pkid, protocol
    ''')
    serializer_class = VpnProtocolSerializer