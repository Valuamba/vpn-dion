from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from djmoney.models.fields import MoneyField

from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_device_tariff.models import VpnDeviceTariff


class SubscriptionPaymentStatus(models.IntegerChoices):
    ON_PAYMENT = 1, _("On Payment")
    WAITING_FOR_PAYMENT = 2, _("Waiting for payment")


class VpnSubscription(TimeStampedUUIDModel):
    user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    tariff = models.ForeignKey(VpnDeviceTariff, related_name="vpn_subscriptions", null=True, on_delete=models.SET_NULL)
    total_price = MoneyField(verbose_name=_("Total Price"), max_digits=14, decimal_places=2, default_currency='RUB')
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    status = models.IntegerField(verbose_name=_("Subscription status"), choices=SubscriptionPaymentStatus.choices)

    @property
    def user_data(self):
        return self.user

    @property
    def tariff_data(self):
        return self.tariff

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(VpnSubscription, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'total: {self.total_price}'


class VpnSubscriptionBound(models.Model):
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="vpn_items", null=True, on_delete=models.SET_NULL)

    @property
    def vpn_subscription_data(self):
        return self.vpn_subscription

    class Meta:
        abstract = True