import ast

from django.shortcuts import render

# Create your views here.
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet

from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, ReadVpnSubscriptionSerializer


class VpnSubscriptionViewSet(ModelViewSet):
    queryset = VpnSubscription.objects.all()
    serializer_class = VpnSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        vpn_items = request.data['vpn_items']
        vpn_items = [ast.literal_eval(item) for item in vpn_items]

        new_vpn_items = []
        for vpn_item in vpn_items:
            new_vpn_item = VpnItemCreateSerializer().create({
                **vpn_item,
                # 'vpn_subscription_id': vpn_subscription.pkid
            }
            )
            new_vpn_items.append(new_vpn_item.id)

        subscription = super(VpnSubscriptionViewSet, self).create(request, *args, **kwargs)

        return subscription
