import decimal

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel


class VpnDurationPrice(TimeStampedUUIDModel):
    month_duration = models.PositiveIntegerField(verbose_name=_("Month duration"), validators=[MinValueValidator(1)], unique=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='RUB')

    class Meta:
        get_latest_by="month_duration"
        verbose_name=_("Vpn duration price")
        verbose_name_plural = "Vpn durations prices"

    def __str__(self):
        return f"{self.month_duration} month"

    @property
    def currency(self) -> str:
        return self.price.currency

    def get_default_month(self):
        return VpnDurationPrice.objects.get(month_duration=1)

    @property
    def amount(self) -> decimal.Decimal:
        return self.price.amount