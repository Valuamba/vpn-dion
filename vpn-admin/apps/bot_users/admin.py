from django.contrib import admin

# Register your models here.
from apps.bot_users.models import BotUser


class BotUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'first_name', 'last_name', 'is_bot_blocked', 'referral_value', 'created_at', 'update_at']


admin.site.register(BotUser, BotUserAdmin)