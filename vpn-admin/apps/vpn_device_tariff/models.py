import decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_country.models import VpnCountry
from apps.vpn_duration_tariff.models import VpnDurationPrice


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
        default_duration_price = self.duration.get_default_month()
        initial_price = self.devices_number * default_duration_price.amount * self.duration_data.month_duration
        return round(initial_price)

    def discounted_price(self, devices = []):
        discount = decimal.Decimal((100 - self.discount_percentage) / 100)

        duration_price = decimal.Decimal(0.0)
        for i in range(self.devices_number):
            device_amount = self.duration_data.amount
            if i <= len(devices) - 1:
                device = devices[i]
                country = VpnCountry.objects.get(pkid=device['country_id'])
                country_discount = decimal.Decimal((100 - country.discount_percentage) / 100)
                device_amount = self.duration_data.amount * country_discount
            duration_price += device_amount

        discounted_price = duration_price * discount

        return round(discounted_price)

    @property
    def total_discount(self):
        discount_percentage = round(100 - ((self.discounted_price() * 100) / self.initial_price))
        return round(discount_percentage)

    def __str__(self):
        return f'VPN: {self.operation} {self.devices_number} devices with {self.discount_percentage}% discount'