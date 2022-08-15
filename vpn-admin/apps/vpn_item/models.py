import base64
from io import BytesIO

from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscriptionBound
import qrcode


class VpnItem(TimeStampedUUIDModel, VpnSubscriptionBound):
    instance = models.ForeignKey(VpnInstance, related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    protocol = models.ForeignKey(VpnProtocol, related_name="vpn_items", null=False, on_delete=models.CASCADE)

    public_key = models.CharField(verbose_name=_("Public Key"), max_length=200)
    private_key = models.CharField(verbose_name=_("Private Key"), max_length=200)
    address = models.CharField(verbose_name=_("Address"), max_length=100)
    dns = models.CharField(verbose_name=_("DNS"), max_length=100)
    preshared_key = models.CharField(verbose_name=_("Preshared key"), max_length=100)
    endpoint = models.CharField(verbose_name=_("Endpoint"), max_length=100)
    allowed_ips = models.CharField(verbose_name=_("Allowed IP's"), max_length=500)
    config_name = models.CharField(verbose_name=_("Config Name"), max_length=200)

    def generate_qrcode_bytes(self):
        qr_str = f'''[Interface]
  PrivateKey = {self.private_key}
  Address = {self.address}
  DNS = {self.dns}

  [Peer]
  PublicKey = {self.public_key}
  PresharedKey = {self.preshared_key}
  Endpoint = {self.endpoint}
  AllowedIPs = {self.allowed_ips}'''

        internal_image = qrcode.make(qr_str)
        file_like_image = BytesIO()
        internal_image.save(file_like_image, format="PNG")
        file_like_image.seek(0)
        return file_like_image

    def get_base64_qrcode(self):
        image = self.generate_qrcode_bytes()
        base64_image_data = base64.b64encode(image.read()).decode("utf-8")
        return "data:image/png;base64", base64_image_data

    @property
    def vpn_subscription_data(self):
        return self.vpn_subscription

    @property
    def instance_data(self):
        return self.instance

    @property
    def protocol_data(self):
        return self.protocol

    def __str__(self):
        return self.config_name