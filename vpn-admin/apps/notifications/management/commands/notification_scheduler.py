import logging
import subprocess
import time

from django.conf import settings
from django.core.management import BaseCommand
from django.utils import timezone

from apps.notifications.models import Notification

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            now = timezone.now()
            notifications = Notification.filter_for_date(now)
            logger.info(
                "Running scheduler %d notifications found.", notifications.count()
            )

            for notification in notifications:
                subprocess.Popen(
                    ["python", settings.BASE_DIR / "manage.py", "send_notification", str(notification.pkid)]
                )

            time.sleep(40)
