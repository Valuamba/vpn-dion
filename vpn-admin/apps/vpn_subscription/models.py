import decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from djmoney.models.fields import MoneyField

from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
# from apps.vpn_item.models import VpnItem


class SubscriptionPaymentStatus(models.TextChoices):
    PAID_SUCCESSFULLY = 'paid', _("On Payment")
    WAITING_FOR_PAYMENT = 'waiting for payment', _("Waiting for payment")
    PAYMENT_WAS_FAILED = 'payment_was_failed', _("Payment was failed")


class VpnSubscription(TimeStampedUUIDModel):
    user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    tariff = models.ForeignKey(VpnDeviceTariff, related_name="vpn_subscriptions", null=True, on_delete=models.SET_NULL)
    status = models.CharField(verbose_name=_("Subscription status"), choices=SubscriptionPaymentStatus.choices, max_length=100)
    is_referral = models.BooleanField(verbose_name=_("Is referral"), default=False)
    subscription_end = models.DateTimeField(verbose_name=_('End of subscription'), null=False)
    price = MoneyField(verbose_name=_("Total Price"), max_digits=14, decimal_places=2, default_currency='RUB')
    discount = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    @property
    def vpn_items_list(self):
        return self.vpn_items.all()

    @property
    def discounted_price(self):
        vpn_items = self.vpn_items.all()
        return self.tariff.discounted_price([{'country_id': item.instance.country.pkid } for item in vpn_items])

    @property
    def discount(self):
        return self.tariff.total_discount

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

    # def __str__(self):
    #     return f'total: {self.total_price}'


class VpnSubscriptionBound(models.Model):
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="vpn_items", null=True, on_delete=models.CASCADE)

    @property
    def vpn_subscription_data(self):
        return self.vpn_subscription

    class Meta:
        abstract = True