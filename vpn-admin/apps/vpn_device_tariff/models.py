from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_duration_tariff.models import VpnDurationPrice


class VpnDeviceTariff(TimeStampedUUIDModel):
    class OperationType(models.TextChoices):
        EQUAL = "equal", _("=")
        GREATER_THAN_OR_EQUAL = "greater_than_or_equal", _(">=")

    duration = models.ForeignKey(VpnDurationPrice, verbose_name=_("Duration"), related_name="vpn_subscriptions", on_delete=models.CASCADE)
    devices_number = models.PositiveIntegerField(verbose_name=_("Number of devices"), validators=[MinValueValidator(1)])
    operation = models.CharField(verbose_name=_("Device operation"), choices=OperationType.choices, blank=False, max_length=30)
    discount_percentage = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    @property
    def duration_data(self):
        return self.duration

    @property
    def result_price(self):
        amount = self.duration.amount * self.devices_number * self.discount_percentage
        return amount

    def __str__(self):
        return f'VPN: {self.operation} {self.devices_number} devices with {self.discount_percentage}% discount'