import logging

from django.db import models

from lib.telegram import TelegramClient

logger = logging.getLogger(__name__)


class Notification(models.Model):
    text = models.TextField()
    schedule_time = models.DateTimeField(blank=True, null=True)
    was_sent = models.BooleanField(default=False)

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
        client = TelegramClient('5419074929:AAGVK-Q8iss7b2nQiT5kluDscwFF2CsolAo', 'https://api.telegram.org')
        client.send_message(chat_id='395040322', text="Reminder")
       # participant_bot.client.send_message(
       #                  participant.telegram_id, self.text)

        self.was_sent = True
        self.save(update_fields=["was_sent", "telegram_poster_id"])

    @classmethod
    def filter_for_date(cls, date):
        return cls.objects.filter(
            schedule_time__year=date.year,
            schedule_time__month=date.month,
            schedule_time__day=date.day,
            schedule_time__hour=date.hour,
            schedule_time__minute=date.minute,
        )

    class Meta:
        ordering = ("-id",)
