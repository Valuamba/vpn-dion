import logging
import time
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.management import BaseCommand
from django.utils import timezone

from apps.bot_locale.models import MessageLocale
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus, SubReminderState
from lib.freekassa import get_freekassa_checkout
from lib.telegram import TelegramClient

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TelegramClient(settings.BOT_TOKEN, settings.TELEGRAM_API_ORIGIN)

    def handle(self, *args, **kwargs):
        days_duration = 7
        while True:
            try:
                subscriptions = VpnSubscription.objects.filter(subscription_end__lt=timezone.now() + relativedelta(days=days_duration),
                                                               status=SubscriptionPaymentStatus.PAID_SUCCESSFULLY).exclude(reminder_state=SubReminderState.NONE)

                for sub in subscriptions:
                    logger.info(f'Remind user {sub.user_id} with subscription {sub.pkid}')
                    if sub.reminder_state == SubReminderState.SEVEN_DAYS_REMINDER:
                        if sub.subscription_end < timezone.now() + relativedelta(days=days_duration):
                            self.remind(sub.user_id, sub.subscription_end, sub.pkid)
                            sub.reminder_state = SubReminderState.THREE_DAYS_REMINDER
                    elif sub.reminder_state == SubReminderState.THREE_DAYS_REMINDER:
                        if sub.subscription_end < timezone.now() + relativedelta(days=3):
                            self.remind(sub.user_id, sub.subscription_end, sub.pkid)
                            sub.reminder_state = SubReminderState.ONE_DAY_REMINDER
                    elif sub.reminder_state == SubReminderState.ONE_DAY_REMINDER:
                        if sub.subscription_end < timezone.now() + relativedelta(days=1):
                            self.remind(sub.user_id, sub.subscription_end, sub.pkid)
                    sub.save()
            except Exception as e:
                logger.error(f'Error message: {str(e)}')
                raise e
            finally:
                time.sleep(30)

    def remind(self, user_id, subscription_end, subscription_id):
        locale = MessageLocale.objects.get(alias='subReminder')
        text = locale.text.format(
            end_date_loc=subscription_end.strftime("%m.%d.%Y")
        )

        extend_sub_url = settings.WEB_APP_LINK + f'?state=ExtendVpnSubscription&subscription_id={subscription_id}'

        self.client.send_message(user_id, text, inline_keyboard=[
                                         [{
                                             'text': 'Продлить подписку',
                                             'web_app': {
                                                 'url': extend_sub_url
                                             }
                                         }]
                                 ])

