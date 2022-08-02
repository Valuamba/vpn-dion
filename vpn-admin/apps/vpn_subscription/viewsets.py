import ast

from django.shortcuts import render

# Create your views here.
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet

from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, ReadVpnSubscriptionSerializer, \
    UpdateVpnSubscriptionSerializer


class VpnSubscriptionViewSet(ModelViewSet):
    queryset = VpnSubscription.objects.all()
    serializer_class = VpnSubscriptionSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return UpdateVpnSubscriptionSerializer

        return VpnSubscriptionSerializer