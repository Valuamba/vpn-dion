from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel


class VpnProtocolType(models.TextChoices):
    WIREGUARD = "wireguard", _("Wireguard")
    OPEN_VPN = "open_vpn", _("OpenVPN")


class VpnProtocol(TimeStampedUUIDModel):
    protocol = models.CharField(max_length=154, unique=True, choices=VpnProtocolType.choices)
    is_default = models.BooleanField(verbose_name=_("Is default"), default=False)

    class Meta:
        db_table = "vpn_protocols"

    def __str__(self):
        return self.protocol