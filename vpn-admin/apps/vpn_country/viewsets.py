from django.shortcuts import render

# Create your views here.
from django_countries.serializer_fields import CountryField
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.common.models import TimeStampedUUIDModel
from django.db import models

from apps.vpn_country.models import VpnCountry
from apps.vpn_country.serializers import VpnCountrySerializer


class VpnCountryViewSet(ModelViewSet):
    queryset = VpnCountry.objects.filter(vpn_instances__is_online=True)
    serializer_class = VpnCountrySerializer
