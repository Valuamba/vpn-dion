import logging
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from apps.common.models import TimeStampedUUIDModel


logger = logging.getLogger(__name__)


class UserRole(models.TextChoices):
    NEW = "New", _("New")


class BotUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True, verbose_name=_("User ID"), unique=True)
    user_name = models.CharField(verbose_name=_("User Name"), blank=True, max_length=200)
    first_name = models.CharField(verbose_name=_("First Name"), blank=True, max_length=200)
    last_name = models.CharField(verbose_name=_("Last Name"), blank=True, max_length=200)
    is_bot_blocked = models.BooleanField(verbose_name=_("Is Bot Blocked by User"), default=False)
    referral_value = models.CharField(verbose_name=_("Referral value"), max_length=50, blank=False, unique=True, db_index=True)

    id = models.UUIDField(default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    @property
    def referrals_count(self) -> int:
        results =  self.referrals.raw(f'''
            select r.* from bot_users_referralitem as r
            WHERE r.referred_user_id IN (SELECT sub.user_id 
            FROM vpn_subscription_vpnsubscription as sub
			WHERE sub.user_id = {self.user_id}  and sub.status = 'paid'
            GROUP BY sub.user_id  HAVING COUNT(*) > 1)
        ''')
        return len(results)
        # return self.referrals.all().count()

    @property
    def free_referrals_count(self) -> int:
        results = self.referrals.raw(f'''
               select r.* from bot_users_referralitem as r
               WHERE r.referred_user_id IN (SELECT sub.user_id 
               FROM vpn_subscription_vpnsubscription as sub
			   WHERE sub.user_id = {self.user_id}  and sub.status = 'paid'
               GROUP BY sub.user_id  HAVING COUNT(*) > 1)
               and is_activated_reward=false
        ''')
        return len(results)
        # return self.referrals.filter(is_activated_reward=False).count()

    @property
    def free_referrals_data(self):
        return self.referrals.filter(is_activated_reward=False)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class ReferralItem(models.Model):
    referral_owner = models.ForeignKey(BotUser, related_name='referrals', on_delete=models.DO_NOTHING)
    referred_user = models.OneToOneField(BotUser, related_name='referral_item', on_delete=models.DO_NOTHING)
    is_activated_reward = models.BooleanField(verbose_name=_('Is activated reward'), default=False)