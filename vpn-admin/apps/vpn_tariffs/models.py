import decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

from apps.common.models import TimeStampedUUIDModel


class VpnDurationPrice(TimeStampedUUIDModel):
    month_duration = models.PositiveIntegerField(verbose_name=_("Month duration"), validators=[MinValueValidator(1)], unique=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB')

    class Meta:
        get_latest_by="month_duration"
        verbose_name=_("Vpn duration price")
        verbose_name_plural = "Vpn durations prices"
        db_table = "vpn_duration_prices"

    def __str__(self):
        return f"{self.month_duration} month"

    @property
    def currency(self) -> str:
        return self.price.currency

    @property
    def amount(self) -> decimal.Decimal:
        return self.price.amount


class VpnDeviceTariff(TimeStampedUUIDModel):
    class OperationType(models.TextChoices):
        EQUAL = "equal", _("=")
        GREATER_THAN_OR_EQUAL = "greater_than_or_equal", _(">=")

    duration = models.ForeignKey(VpnDurationPrice, verbose_name=_("Duration"), related_name="vpn_subscriptions", on_delete=models.CASCADE)
    devices_number = models.PositiveIntegerField(verbose_name=_("Number of devices"), validators=[MinValueValidator(1)])
    operation = models.CharField(verbose_name=_("Device operation"), choices=OperationType.choices, blank=False, max_length=30)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    class Meta:
        db_table = "vpn_devices"

    @property
    def duration_data(self):
        return self.duration

    @property
    def initial_price(self):
        initial_price = self.devices_number * self.duration.price.amount
        return round(initial_price)

    def __str__(self):
        return f'VPN: {self.operation} {self.devices_number} devices with {self.discount_percentage}% discount'