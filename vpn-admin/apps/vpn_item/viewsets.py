from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemSerializer


class VpnItemViewSet(ModelViewSet):
    queryset = VpnItem.objects.all()
    serializer_class = VpnItemSerializer