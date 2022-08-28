from django.conf import settings
from django.db import models

from apps.bot_users.models import BotUser


class Message(models.Model):
    consumer = models.ForeignKey(BotUser, related_name='feedback_messages', on_delete=models.DO_NOTHING)
    message_id = models.IntegerField()
    
    text = models.TextField()
    
    # Null - Не обработано, True - Обработано, False - игнорируем
    status = models.BooleanField(null=True, blank=True)
    
    receive_date = models.DateTimeField(auto_now_add=True)
    answer_date = models.DateTimeField(null=True, blank=True)
    
    admin_message = models.TextField(null=True, blank=True)
    admin_message_photo = models.ImageField(null=True, blank=True)

    # Use this method in admin list_display to display str instead checkmarks
    def status2str(self):
        if self.status is None:
            return "Unchecked"
        return "Processed" if self.status else "Ignored"
    
    def __str__(self, max_len=75):
        ends = '...' if len(self.text) > max_len else ''
        return f"{self.text}: {self.text[:max_len]}{ends}"
    
    class Meta:
        verbose_name = "Сообщение" if settings.LANGUAGE_CODE == 'ru' else "Message"
        verbose_name_plural = "Сообщения" if settings.LANGUAGE_CODE == 'ru' else "Messages"
        ordering = ['status', '-receive_date']
        db_table = 'feedback_messages'
        