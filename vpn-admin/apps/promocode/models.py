from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.bot_users.models import BotUser
from apps.common.models import TimeStampedUUIDModel


# Create your models here.


class PromoCode(TimeStampedUUIDModel):
    promocode = models.CharField(verbose_name=_("Promocode"), unique=True, max_length=100)
    expires = models.DateField(verbose_name=_("Expires"), null=False)
    discount = models.IntegerField(verbose_name=_("Discount"), null=False, validators=[MinValueValidator(1)])
    applied_by_users = models.ManyToManyField(BotUser, related_name='promocodes')

    def check_promocode(self, user_id):
        user = next((user for user in self.applied_by_users.all() if user.user_id == user_id), None)
        return user is None

    @property
    def count_users(self):
        return self.applied_by_users.count()

    class Meta:
        db_table = 'promocode'