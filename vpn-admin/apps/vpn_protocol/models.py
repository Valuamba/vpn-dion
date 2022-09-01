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

    @classmethod
    def get_defaults(cls):
        results = VpnProtocol.objects.raw('''
SELECT p.pkid, p.protocol, p.is_default FROM public.vpn_protocols as p
INNER JOIN public.vpn_instances_protocols ON vpn_instances_protocols.vpnprotocol_id = p.pkid 
INNER JOIN public.vpn_instances vpn_instances2 ON vpn_instances2.pkid = vpn_instances_protocols.vpninstance_id
WHERE vpn_instances2.is_online=True and p.is_default=True
GROUP BY p.pkid, protocol
''')

        return results

    def __str__(self):
        return self.protocol