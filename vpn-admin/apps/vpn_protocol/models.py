from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.common.models import TimeStampedUUIDModel


class VpnProtocolType(models.TextChoices):
    WIREGUARD = "wireguard", _("Wireguard")
    OPEN_VPN = "open_vpn", _("OpenVPN")


class VpnProtocol(TimeStampedUUIDModel):
    protocol = models.CharField(max_length=154, unique=True, choices=VpnProtocolType.choices)

    def __str__(self):
        return self.protocol