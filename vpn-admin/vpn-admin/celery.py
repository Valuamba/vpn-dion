import os
from __future__ import absolute_import
from celery import Celery
from settings import base
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vpn-admin.settings.development')

app = Celery('vpn-admin')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('vpn-admin.settings.development', namespace='CELERY')

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')