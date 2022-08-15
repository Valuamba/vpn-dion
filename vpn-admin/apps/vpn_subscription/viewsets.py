import ast

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer, ReadVpnSubscriptionSerializer, \
    UpdateVpnSubscriptionSerializer


class UserSubscriptionViewSet(ListAPIView):
    serializer_class = VpnSubscriptionSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return VpnSubscription.objects.filter(user_id=user_id, status__in=[SubscriptionPaymentStatus.PAID_SUCCESSFULLY])


class VpnSubscriptionViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = VpnSubscription.objects.all()
    serializer_class = VpnSubscriptionSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return UpdateVpnSubscriptionSerializer

        return VpnSubscriptionSerializer