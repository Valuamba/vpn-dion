from functools import cached_property
from typing import List
from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_country.models import VpnCountry
from apps.vpn_protocol.models import VpnProtocol
from lib.vpn_server.client import VpnServerApiClient
from lib.vpn_server.datatypes import InstanceStatistic, WgInfo


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

    class Meta:
        db_table = "vpn_instances"

    @property
    def country_data(self):
        return self.country

    @property
    def protocols_data(self):
        return self.protocols

    @cached_property
    def client(self) -> VpnServerApiClient:
        return VpnServerApiClient(api_origin=f'{self.server_protocol}://{self.ip_address}:{self.port}/')

    @cached_property
    def wg_connections(self) -> List[WgInfo]:
        try:
            return self.client.collect_wg_connections()
        except:
            return []

    @property
    def all_connections(self):
        return len(self.wg_connections)

    @property
    def active_connections(self) -> int:
        active_connections = [con.peer for con in self.wg_connections if con.allowed_ips is not None]
        return apps.get_model('vpn_item.VpnItem').objects.filter(private_key__in=active_connections).count()

    @cached_property
    def statistics(self) -> InstanceStatistic:
        try:
            return self.client.collect_statistics()
        except:
            return InstanceStatistic(
                cpu=0,
                networkUpload_b=0,
                network_download_b=0,
                network_download_speed_b=0,
                network_upload_speed_b=0,
                ram=0,
                total_b=0,
            )

    @property
    def cpu(self):
        return round(self.statistics.cpu, 2)

    @property
    def ram(self):
        return int(self.statistics.ram)

    @property
    def network_upload(self):
        return int(self.statistics.networkUpload_b / (10 * 6))

    @property
    def network_download(self):
        return int(self.statistics.network_download_b / (10 * 6))

    @property
    def network_download_speed(self):
        return round(self.statistics.network_download_speed_b / (10 * 6), 2)

    @property
    def network_upload_speed(self):
        return int(self.statistics.network_upload_speed_b / (10 * 6))

    def __str__(self):
        return self.name
