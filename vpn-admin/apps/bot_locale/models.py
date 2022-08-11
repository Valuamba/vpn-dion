import uuid

from django.db import models

# Create your models here.
from apps.common.models import TimeStampedUUIDModel


class MessageLocale(models.Model):
    alias = models.CharField(max_length=1000, primary_key=True)
    text = models.TextField(max_length=1000)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.alias}: {self.text[:30]}"

    class Meta:
        db_table = "MessageLocale"
