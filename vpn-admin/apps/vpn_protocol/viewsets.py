from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class VpnProtocolViewSet(ModelViewSet):
    queryset = VpnProtocol.objects.raw('''
SELECT p.pkid, p.protocol, p.is_default FROM public.vpn_protocols as p
INNER JOIN public.vpn_instances_protocols ON vpn_instances_protocols.vpnprotocol_id = p.pkid 
INNER JOIN public.vpn_instances vpn_instances2 ON vpn_instances2.pkid = vpn_instances_protocols.vpninstance_id
WHERE vpn_instances2.is_online=True
GROUP BY p.pkid, protocol
    ''')
    serializer_class = VpnProtocolSerializer