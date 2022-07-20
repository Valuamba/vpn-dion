from django.contrib import admin

# Register your models here.
from apps.bot_users.models import BotUser


admin.site.register(BotUser)