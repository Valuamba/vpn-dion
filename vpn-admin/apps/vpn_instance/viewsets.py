from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.vpn_instance.models import VpnInstance
from apps.vpn_instance.serializers import VpnInstanceSerializer


class VpnInstanceViewSet(ModelViewSet):
    queryset = VpnInstance.objects.all()
    serializer_class = VpnInstanceSerializer