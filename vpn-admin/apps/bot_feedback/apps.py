from django.apps import AppConfig
from django.conf import settings


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bot_feedback'

    verbose_name = "Бот" if settings.LANGUAGE_CODE == 'ru' else "Bot"
    
