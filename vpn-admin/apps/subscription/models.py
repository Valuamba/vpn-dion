from functools import cached_property

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from djmoney.models.fields import MoneyField

from apps.bot_assets.models import VpnCountry, VpnProtocol
from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel, Currency
from lib.vpn_server.client import VpnServerApiClient


class SubscriptionPaymentStatus(models.IntegerChoices):
    ON_PAYMENT = 1, _("On Payment")
    WAITING_FOR_PAYMENT = 2, _("Waiting for payment")


class VpnSubscription(TimeStampedUUIDModel):
    user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    amount_of_devices = models.IntegerField()
    amount_of_month = models.IntegerField(verbose_name=_("Amount of months"), null=False)
    subscription_datetime_utc = models.DateTimeField(verbose_name=_("Subscription date time"))
    total_price = MoneyField(verbose_name=_("Total Price"), max_digits=14, decimal_places=2, default_currency='RUB')
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    status = models.IntegerField(verbose_name=_("Subscription status"), choices=SubscriptionPaymentStatus.choices)

    def __str__(self):
        return f'devices: {self.amount_of_devices}, months: {self.amount_of_month}, total: {self.total_price}'


class VpnItem(TimeStampedUUIDModel):
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    instance = models.ForeignKey("Instance", related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    protocol = models.ForeignKey(VpnProtocol, related_name="vpn_items", null=False, on_delete=models.CASCADE)
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


class Instance(TimeStampedUUIDModel):

    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(VpnCountry, verbose_name=_("Country"), related_name="instances", null=True, on_delete=models.SET_NULL)
    protocols = models.ManyToManyField(VpnProtocol, related_name="instances")
    is_online = models.BooleanField()

    @cached_property
    def client(self) -> VpnServerApiClient:
        return VpnServerApiClient(api_origin='http://localhost:5000')

    def __str__(self):
        return self.name