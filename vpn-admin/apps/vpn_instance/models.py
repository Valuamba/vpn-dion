from functools import cached_property

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_country.models import VpnCountry
from apps.vpn_protocol.models import VpnProtocol
from lib.vpn_server.client import VpnServerApiClient


class VpnInstance(TimeStampedUUIDModel):

    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(VpnCountry, verbose_name=_("Country"), related_name="vpn_instances", null=True, on_delete=models.SET_NULL)
    protocols = models.ManyToManyField(VpnProtocol, related_name="instances")
    is_online = models.BooleanField()

    @property
    def country_data(self):
        return self.country

    @property
    def protocols_data(self):
        return self.protocols

    @cached_property
    def client(self) -> VpnServerApiClient:
        return VpnServerApiClient(api_origin='http://localhost:5000')

    def __str__(self):
        return self.name