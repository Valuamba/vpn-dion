import json
import logging
import os

from django.conf import settings
from django.core.management import BaseCommand

from apps.bot_locale.models import MessageLocale

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        locales = []
        with open(settings.BOT_LOCALES_PATH, 'r') as f:
            text = f.read()
            locales = json.loads(text)
        db_locales = MessageLocale.objects.all()

        for l in locales:
            if not next(d for d in db_locales if d.alias == l['alias']):
                logger.info(f'Creating locale: {l["alias"]}')
                MessageLocale.objects.create(alias=l['alias'], text=l['text'])