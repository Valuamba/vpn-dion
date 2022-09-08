import logging

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from apps.bot_locale.models import MessageLocale
from apps.common.models import TimeStampedUUIDModel
from apps.vpn_subscription.models import VpnSubscription
from lib.telegram import TelegramClient

logger = logging.getLogger(__name__)


class SubscriptionNotificationType(models.TextChoices):
    SEVEN_DAYS_REMINDER = 'sevenDaysReminder', _("Seven Days Reminder")
    THREE_DAYS_REMINDER = 'threeDaysReminder', _("Three Days Reminder")
    ONE_DAY_REMINDER = 'oneDayReminder', _("One Day Reminder")
    SUBSCRIPTION_OUTDATED = 'subscriptionOutdated', _("Subscription Outdated")


class Notification(TimeStampedUUIDModel):
    vpn_subscription = models.ForeignKey(VpnSubscription, related_name="notifications", null=True, on_delete=models.CASCADE)
    schedule_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(verbose_name=_("Notification status"), choices=SubscriptionNotificationType.choices, max_length=150)
    was_sent = models.BooleanField(default=False)

    class Meta:
        db_table = "notifications"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Notification, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

        if not self.schedule_time and not self.was_sent:
            self.send()

    def send(self):
        if self.status == SubscriptionNotificationType.THREE_DAYS_REMINDER:
            locale = MessageLocale.objects.get(alias='threeDaysSubscriptionReminder').text
        if self.status == SubscriptionNotificationType.ONE_DAY_REMINDER:
            locale = MessageLocale.objects.get(alias='oneDaySubscriptionReminder').text
        if self.status == SubscriptionNotificationType.SUBSCRIPTION_OUTDATED:
            locale = MessageLocale.objects.get(alias='subscriptionOutdated').text

        extend_loc = MessageLocale.objects.get(alias='extendSubscriptionInline').text
        extend_sub_url = settings.WEB_APP_LINK + f'?state=ExtendVpnSubscription&subscription_id={self.vpn_subscription.pkid}'
        self.client.send_message(chat_id=self.vpn_subscription.user.user_id, text=locale,
                                 inline_keyboard=[
                                     [
                                         {'text': extend_loc, 'web_app': { 'url': extend_sub_url } }
                                     ]
                                 ])

        self.was_sent = True
        self.save()

    @cached_property
    def client(self) -> TelegramClient:
        return TelegramClient(settings.BOT_TOKEN, settings.TELEGRAM_API_ORIGIN)

    @classmethod
    def send_notification_about_successful_payment(cls, subscription):
        show_subscription_details = MessageLocale.objects.get(alias='showSubscriptionDetails').text
        sub_payed_successfully = MessageLocale.objects.get(alias='subscriptionPayedSuccessfully').text
        client = TelegramClient(settings.BOT_TOKEN, settings.TELEGRAM_API_ORIGIN)
        client.send_message(chat_id=subscription.user.user_id, text=sub_payed_successfully,
                            inline_keyboard= [[{ 'text': show_subscription_details, 'callback_data': f'vpn-subscription:{subscription.pkid}'}]])

    @classmethod
    def remove_unsended_notifications(cls, sub_id):
        return cls.objects.filter(
            vpn_subscription_id=sub_id,
            was_sent=False
        ).delete()


    @classmethod
    def create_default_subscription_reminders(cls, sub_id, sub_end):
        t1 = timezone.now() + timezone.timedelta(minutes=5)
        t2 = timezone.now() + timezone.timedelta(minutes=20)
        t3 = timezone.now() + timezone.timedelta(minutes=40)
        cls.objects.create(
            vpn_subscription_id=sub_id,
            schedule_time=t1, #sub_end + timezone.timedelta(days=-3),
            status=SubscriptionNotificationType.THREE_DAYS_REMINDER
        )

        cls.objects.create(
            vpn_subscription_id=sub_id,
            schedule_time=t2, #sub_end + timezone.timedelta(days=-1),
            status=SubscriptionNotificationType.ONE_DAY_REMINDER
        )

        cls.objects.create(
            vpn_subscription_id=sub_id,
            schedule_time=t3, #sub_end,
            status=SubscriptionNotificationType.SUBSCRIPTION_OUTDATED
        )

    @classmethod
    def filter_for_date(cls, date):
        return cls.objects.filter(
            schedule_time__year=date.year,
            schedule_time__month=date.month,
            schedule_time__day=date.day,
            schedule_time__hour=date.hour,
            schedule_time__minute=date.minute,
            was_sent=False
        )

    class Meta:
        ordering = ("-id",)
