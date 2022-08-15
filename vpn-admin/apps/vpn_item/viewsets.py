import io
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemSerializer, CreateVpnItemSerializer


class VpnItemViewSet(ModelViewSet):
    queryset = VpnItem.objects.all()

    def get_serializer_class(self):
        if self.request.method in 'POST':
            return CreateVpnItemSerializer

        return VpnItemSerializer

    @action(methods=['post'], detail=False, url_path="multiple/create")
    def multiple_create(self, request, *args, **kwargs):
        data = json.loads(request.data)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubscriptionVpnItemsViewSet(ListAPIView):
    serializer_class = VpnItemSerializer

    def get_queryset(self):
        subscription_id = self.kwargs['subscription_id']
        return VpnItem.objects.filter(vpn_subscription_id=subscription_id)


@api_view(['GET'])
def get_vpn_item_qrcode(request, device_id):
    vpn_item = VpnItem.objects.get(pkid=device_id)
    qrcode_b = vpn_item.generate_qrcode_bytes()
    return HttpResponse(qrcode_b.getvalue(), content_type="image/png")
