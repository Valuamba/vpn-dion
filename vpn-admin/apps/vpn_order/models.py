from django.core.validators import MinValueValidator
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models import EmailField

from apps.bot.models import BotUser
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_tariffs.models import VpnDeviceTariff
from lib.vpn_server.client import VpnServerApiClient


class VpnCountry(TimeStampedUUIDModel):
    place = CountryField(verbose_name=_("Country"), blank_label="(select country)", unique=True, null=False)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Country discount percentage"), default=0)
    is_default = models.BooleanField(verbose_name=_("Is default"), default=False)
    locale_ru = models.CharField(verbose_name=_("Locale RU"), max_length=200)

    class Meta:
        verbose_name = "Vpn country"
        verbose_name_plural = "Vpn Countries"
        db_table = "vpn_countries"

    @property
    def country(self) -> str:
        return self.place.name

    def __str__(self):
        return f'Country {self.place} with discount {self.discount_percentage}'


class VpnProtocol(TimeStampedUUIDModel):
    class VpnProtocolType(models.TextChoices):
        WIREGUARD = "wireguard", _("Wireguard")
        OPEN_VPN = "open_vpn", _("OpenVPN")

    name = models.CharField(max_length=154, unique=True, choices=VpnProtocolType.choices)
    is_default = models.BooleanField(verbose_name=_("Is default"), default=False)

    class Meta:
        db_table = "vpn_protocols"

    def __str__(self):
        return self.name


class PromoCode(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Promo code"), unique=True, max_length=100)
    expires = models.DateField(verbose_name=_("Expires"), null=False)
    discount = models.IntegerField(verbose_name=_("Discount"), null=False, validators=[MinValueValidator(1)])
    applied_by_users = models.ManyToManyField(BotUser, related_name='promo_codes')

    class Meta:
        db_table = 'promo_code'


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

    def __str__(self):
        return self.name


class VpnSubscription(TimeStampedUUIDModel):
    class SubscriptionPaymentStatus(models.TextChoices):
        PAID_SUCCESSFULLY = 'paid', _("Paid")
        WAITING_FOR_PAYMENT = 'waiting for payment', _("Waiting for payment")
        PAYMENT_WAS_FAILED = 'payment_was_failed', _("Payment was failed")
        OUTDATED = 'outdated', _("Outdated")

    month_duration = models.PositiveIntegerField(verbose_name=_("Month duration"), validators=[MinValueValidator(0)], null=True)
    days_duration = models.PositiveIntegerField(verbose_name=_("Days duration"), validators=[MinValueValidator(0)], null=True)
    devices_number = models.PositiveIntegerField(verbose_name=_("Number of devices"), validators=[MinValueValidator(1)])
    status = models.CharField(verbose_name=_("Subscription status"), choices=SubscriptionPaymentStatus.choices, max_length=100)
    is_referral = models.BooleanField(verbose_name=_("Is referral"), default=False)
    price = MoneyField(verbose_name=_("Total Price"), max_digits=14, decimal_places=2, default_currency='RUB', null=True)
    discount = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    subscription_end = models.DateTimeField(verbose_name=_('End of subscription'), null=False)

    promo_code = models.ForeignKey(PromoCode, related_name="vpn_subscriptions", null=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    tariff = models.ForeignKey(VpnDeviceTariff, related_name="vpn_subscriptions", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "vpn_subscriptions"


class VpnItem(TimeStampedUUIDModel):
    instance = models.ForeignKey(VpnInstance, related_name="vpn_items", null=True, on_delete=models.SET_NULL)
    protocol = models.ForeignKey(VpnProtocol, related_name="vpn_items", null=False, on_delete=models.CASCADE)

    public_key = models.CharField(verbose_name=_("Public Key"), max_length=200)
    private_key = models.CharField(verbose_name=_("Private Key"), max_length=200)
    address = models.CharField(verbose_name=_("Address"), max_length=100)
    dns = models.CharField(verbose_name=_("DNS"), max_length=100)
    preshared_key = models.CharField(verbose_name=_("Pre-shared key"), max_length=100)
    endpoint = models.CharField(verbose_name=_("Endpoint"), max_length=100)
    allowed_ips = models.CharField(verbose_name=_("Allowed IP's"), max_length=500)
    config_name = models.CharField(verbose_name=_("Config Name"), max_length=200)
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="vpn_items", null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "vpn_items"

    @property
    def vpn_subscription_data(self):
        return self.vpn_subscription

    @property
    def instance_data(self):
        return self.instance

    @property
    def protocol_data(self):
        return self.protocol

    @property
    def country_name(self):
        return self.instance.country.country

    @property
    def protocol_name(self):
        return self.protocol.name

    def __str__(self):
        return self.config_name


class VpnPaymentTransaction(TimeStampedUUIDModel):
    email = EmailField(verbose_name=_("Email"), blank=True)
    phone = PhoneNumberField(verbose_name=_("Phone"), null=True)
    sign = models.CharField(verbose_name=_("Sign"), max_length=200, blank=False)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    currency_id = models.CharField(verbose_name=_("Currency ID"), max_length=50, null=False)
    subscription = models.ForeignKey(VpnSubscription, related_name="payment_transactions", on_delete=models.CASCADE)
    promocode = models.CharField(verbose_name=_("Promocode"), blank=True, max_length=100)

    class Meta:
        db_table = "vpn_payment_transaction"