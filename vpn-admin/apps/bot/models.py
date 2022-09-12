import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class BotMessageLocale(models.Model):
    alias = models.CharField(max_length=1000, primary_key=True)
    text = models.TextField(max_length=2000)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.alias}: {self.text[:30]}"

    class Meta:
        db_table = "message_locale"


class BotUser(models.Model):
    class UserRole(models.TextChoices):
        NEW = "New", _("New")
    user_id = models.BigIntegerField(primary_key=True, verbose_name=_("User ID"), unique=True)
    user_name = models.CharField(verbose_name=_("User Name"), blank=True, max_length=200)
    first_name = models.CharField(verbose_name=_("First Name"), blank=True, max_length=200)
    last_name = models.CharField(verbose_name=_("Last Name"), blank=True, max_length=200)
    is_bot_blocked = models.BooleanField(verbose_name=_("Is Bot Blocked by User"), default=False)
    referral_value = models.CharField(verbose_name=_("Referral value"), max_length=50, blank=False, unique=True, db_index=True)

    id = models.UUIDField(default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bot_user"

    def __str__(self):
        if self.user_name:
            return self.user_name
        elif self.first_name or self.last_name:
            return f'{self.last_name} {self.first_name}'
        else:
            return str(self.user_id)

    @property
    def referral_link(self):
        return f'https://t.me/{settings.BOT_USER_NAME}?start={self.referral_value}'

    @property
    def referrals_count(self) -> int:
        results =  self.referrals.raw(f'''
           select r.* from referral_items as r
            WHERE referral_owner_id={self.user_id} and r.referred_user_id IN (
				SELECT sub.user_id FROM vpn_subscriptions as sub
				WHERE sub.status = 'paid' and sub.is_referral = false
				GROUP BY sub.user_id  
				HAVING COUNT(*) > 0
			)
        ''')
        return len(results)
        # return self.referrals.all().count()

    @property
    def free_referrals_count(self) -> int:
        return len(self.free_referrals_data)

    @property
    def free_referrals_data(self):
        return self.referrals.raw(f'''
               select r.* from referral_items as r
                    WHERE referral_owner_id={self.user_id} and r.referred_user_id IN (
                        SELECT sub.user_id FROM vpn_subscriptions as sub
                        WHERE sub.status = 'paid' and sub.is_referral = false
                        GROUP BY sub.user_id  
                        HAVING COUNT(*) > 0
                    )
                    and is_activated_reward=false
                ''')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class ReferralItem(models.Model):
    referral_owner = models.ForeignKey(BotUser, related_name='referrals', on_delete=models.CASCADE)
    referred_user = models.OneToOneField(BotUser, related_name='referral_item', on_delete=models.CASCADE)
    is_activated_reward = models.BooleanField(verbose_name=_('Is activated reward'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "referral_items"


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