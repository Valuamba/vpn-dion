import json
import logging
import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from apps.bot_locale.models import MessageLocale

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **kwargs):
        locales = []
        with open(settings.BOT_LOCALES_PATH, 'r') as f:
            text = f.read()
            locales = json.loads(text)
        MessageLocale.objects.all().delete()

        new_locales = []
        for l in locales:
            logger.info(f'Creating locale: {l["alias"]}')
            loc = MessageLocale(alias=l['alias'], text=l['text'])
            new_locales.append(loc)

        MessageLocale.objects.bulk_create(new_locales)