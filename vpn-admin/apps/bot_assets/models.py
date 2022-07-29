from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from apps.common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class VpnDurationPrice(TimeStampedUUIDModel):
    month_duration = models.PositiveIntegerField(verbose_name=_("Month duration"), validators=[MinValueValidator(1)], unique=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB')

    class Meta:
        get_latest_by="month_duration"
        verbose_name=_("Vpn duration price")
        verbose_name_plural = "Vpn durations prices"

    def __str__(self):
        return f"{self.month_duration} month"


class VpnSubscriptionOffer(TimeStampedUUIDModel):
    class OperationType(models.TextChoices):
        EQUAL = "equal", _("=")
        GREATER_THAN_OR_EQUAL = "greater_than_or_equal", _(">=")

    duration = models.ForeignKey(VpnDurationPrice, verbose_name=_("Duration"), related_name="vpn_subscriptions", on_delete=models.CASCADE)
    devices_number = models.PositiveIntegerField(verbose_name=_("Number of devices"), validators=[MinValueValidator(1)])
    operation = models.CharField(verbose_name=_("Device operation"), choices=OperationType.choices, blank=False, max_length=30)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    def __str__(self):
        return f'VPN: {self.operation} {self.devices_number} devices with {self.discount_percentage}% discount'


class VpnCountry(TimeStampedUUIDModel):
    country = CountryField(verbose_name=_("Country"), blank_label="(select country)", unique=True, null=False)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Country discount percentage"), default=0)

    class Meta:
        verbose_name = "Vpn country"
        verbose_name_plural = "Vpn Countries"

    def __str__(self):
        return f'Country {self.country} with discount {self.discount_percentage}'


class VpnProtocolType(models.TextChoices):
    WIREGUARD = "wireguard", _("Wireguard")
    OPEN_VPN = "open_vpn", _("OpenVPN")


class VpnProtocol(TimeStampedUUIDModel):
    protocol = models.CharField(max_length=154, unique=True, choices=VpnProtocolType.choices)

    def __str__(self):
        return self.protocol