import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel


class UserRole(models.TextChoices):
    NEW = "New", _("New")


class BotUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True, verbose_name=_("User ID"), unique=True)
    user_name = models.CharField(verbose_name=_("User Name"), blank=True, max_length=200)
    first_name = models.CharField(verbose_name=_("First Name"), blank=True, max_length=200)
    last_name = models.CharField(verbose_name=_("Last Name"), blank=True, max_length=200)
    is_bot_blocked = models.BooleanField(verbose_name=_("Is Bot Blocked by User"), default=False)

    id = models.UUIDField(default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
