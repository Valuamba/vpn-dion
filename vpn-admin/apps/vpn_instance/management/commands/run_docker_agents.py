import logging
import random

import docker
from django.core.management import BaseCommand
from django.conf import settings
from django_countries.data import COUNTRIES

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = docker.from_env()
        containers = []
        for i in range(settings.NUMBER_CONTAINERS):
            containers.append({"port": 33440 + i, "name": f"{settings.VPN_PREFIX}{i}"})

        for c in containers:
            logger.info(f'Run [{c["name"]} container on port [{c["port"]}]')
            client.containers.run(
                image=settings.IMAGE_NAME,
                ports={
                    5000: c["port"]
                },
                name=c["name"],
                tty=True,
                stdin_open=True,
                detach=True,
                # network_mode="host"
            )