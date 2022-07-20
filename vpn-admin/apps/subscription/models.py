from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel


class SubscriptionAmountOfMonth(models.IntegerChoices):
    ONE = 1, _("One")
    THREE = 3, _("Three")
    SIX = 6, _("SIX")
    TWELVE = 12, _("Twelve")


class SubscriptionPaymentStatus(models.IntegerChoices):
    ON_PAYMENT = 1, _("On Payment")
    WAITING_FOR_PAYMENT = 2, _("Waiting for payment")


class Currency(models.TextChoices):
    RUB = "RUB", _("Rub")
    USD = "USD", _("Usd")


class VpnSubscription(TimeStampedUUIDModel):
    user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    amount_of_devices = models.IntegerField()
    amount_of_month = models.IntegerField(verbose_name=_("Amount of months"), choices=SubscriptionAmountOfMonth.choices)
    subscription_datetime_utc = models.DateTimeField(verbose_name=_("Subscription date time"))
    currency = models.CharField(verbose_name=_("Currency"), choices=Currency.choices)
    total_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)