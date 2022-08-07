import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Currency(models.TextChoices):
    RUB = "RUB", _("RUB")
    USD = "USD", _("USD")
