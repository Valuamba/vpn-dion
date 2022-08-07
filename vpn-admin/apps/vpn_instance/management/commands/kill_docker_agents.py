import logging

import docker
from django.core.management import BaseCommand
from django.conf import settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = docker.from_env()
        containers = client.containers.list(all=True)
        vpn_containers = [c for c in containers if c.name.startswith(settings.VPN_PREFIX)]
        for c in vpn_containers:
            logger.info(f"Remove container {c.name}")
            c.stop()
            c.remove()