from functools import cached_property

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_country.models import VpnCountry
from apps.vpn_protocol.models import VpnProtocol
from lib.vpn_server.client import VpnServerApiClient


class VpnInstance(TimeStampedUUIDModel):
    class HttpProtocol(models.TextChoices):
        HTTP = "http", _("HTTP")
        HTTPS = "https", _("HTTPS")

    ip_address = models.GenericIPAddressField()
    port = models.IntegerField()
    server_protocol = models.CharField(verbose_name=_("Server protocol"), max_length=5, blank=False, choices=HttpProtocol.choices)
    name = models.CharField(max_length=100)
    mac = models.CharField(verbose_name=_("MAC"), max_length=200, blank=True)
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
        return VpnServerApiClient(api_origin=f'{self.server_protocol}://{self.ip_address}:{self.port}/')

    # def get_online(self):
    #     return VpnInstance.objects.filter(is_online=True)

    # def get_all(self):
    #     return VpnInstance.objects.all()

    def __str__(self):
        return self.name
