import decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _
# Create your models here.
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel
# from apps.vpn_device_tariff.models import VpnDeviceTariff
# from apps.vpn_item.models import VpnItem


class SubReminderState(models.IntegerChoices):
    THREE_DAYS_REMINDER = 3, _("Reminded for three days")
    SEVEN_DAYS_REMINDER = 7, _("Reminded for seven days")
    ONE_DAY_REMINDER = 1, _("Reminded for one day")
    NONE = 0, _("Ended")


class SubscriptionPaymentStatus(models.TextChoices):
    PAID_SUCCESSFULLY = 'paid', _("Paid")
    WAITING_FOR_PAYMENT = 'waiting for payment', _("Waiting for payment")
    PAYMENT_WAS_FAILED = 'payment_was_failed', _("Payment was failed")
    OUTDATED = 'outdated', _("Outdated")


class VpnSubscription:
    month_duration = models.PositiveIntegerField(verbose_name=_("Month duration"), validators=[MinValueValidator(0)], null=True)
    days_duration = models.PositiveIntegerField(verbose_name=_("Days duration"), validators=[MinValueValidator(0)], null=True)
    devices_number = models.PositiveIntegerField(verbose_name=_("Number of devices"), validators=[MinValueValidator(1)])
    status = models.CharField(verbose_name=_("Subscription status"), choices=SubscriptionPaymentStatus.choices, max_length=100)
    is_referral = models.BooleanField(verbose_name=_("Is referral"), default=False)
    price = MoneyField(verbose_name=_("Total Price"), max_digits=14, decimal_places=2, default_currency='RUB', null=True)
    discount = models.PositiveIntegerField(verbose_name=_("Discount percentage"), default=0)

    subscription_end = models.DateTimeField(verbose_name=_('End of subscription'), null=False)
    reminder_state = models.IntegerField(verbose_name=_("Reminder status"), choices=SubReminderState.choices)

    # user = models.ForeignKey(BotUser, related_name="vpn_subscriptions", on_delete=models.CASCADE)
    # tariff = models.ForeignKey(VpnDeviceTariff, related_name="vpn_subscriptions", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "vpn_subscriptions"

    @property
    def vpn_items_list(self):
        return self.vpn_items.all()

    @property
    def discounted_price(self):
        vpn_items = self.vpn_items.all()
        return self.tariff.price([{'country_id': item.instance.country.pkid } for item in vpn_items])

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

    @classmethod
    def get_active(cls, subscription_id, date):
        return cls.objects.get(
            pkid=subscription_id
        )

    # def __str__(self):
    #     return f'total: {self.total_price}'


class VpnPaymentTransaction:
    email = EmailField(verbose_name=_("Email"), blank=True)
    phone = PhoneNumberField(verbose_name=_("Phone"), null=True)
    sign = models.CharField(verbose_name=_("Sign"), max_length=200, blank=False)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    currency_id = models.CharField(verbose_name=_("Currency ID"), max_length=50, null=False)
    # subscription = models.ForeignKey(VpnSubscription, related_name="payment_transactions", on_delete=models.CASCADE)
    promocode = models.CharField(verbose_name=_("Promocode"), blank=True, max_length=100)

    class Meta:
        db_table = "vpn_payment_transaction"