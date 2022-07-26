from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel, Currency
from apps.subscription.models import VpnSubscription
from apps.vpn_instance.models import Instance


class VpnItem(TimeStampedUUIDModel):
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    instance = models.ForeignKey(Instance, related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    public_key = models.CharField(verbose_name=_("Public Key"), max_length=200)
    private_key = models.CharField(verbose_name=_("Private Key"), max_length=200)
    address = models.CharField(verbose_name=_("Address"), max_length=100)
    dns = models.CharField(verbose_name=_("DNS"), max_length=100)
    preshared_key = models.CharField(verbose_name=_("Preshared key"), max_length=100)
    endpoint = models.CharField(verbose_name=_("Endpoint"), max_length=100)
    allowed_ips = models.CharField(verbose_name=_("Allowed IP's"), max_length=500)
    config_name = models.CharField(verbose_name=_("Config Name"), max_length=200)

    def __str__(self):
        return self.config_name


class VpnProduct(TimeStampedUUIDModel):
    key = models.CharField(verbose_name=_("Key"), max_length=200, unique=True, blank=False)
    default_price = models.DecimalField(verbose_name=_("Default price"), max_digits=8, decimal_places=2, default=0.0)
    currency = models.CharField(verbose_name=_("Currency"), choices=Currency.choices, max_length=3)

    def __str__(self):
        return self.key