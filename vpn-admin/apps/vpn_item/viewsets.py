import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
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