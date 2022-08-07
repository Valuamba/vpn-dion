import logging
import random

import docker
from django.core.management import BaseCommand
from django.conf import settings
from django_countries.data import COUNTRIES

from apps.vpn_country.models import VpnCountry
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = docker.from_env()

        protocols = VpnProtocol.objects.all()
        countries = VpnCountry.objects.all()

        containers = client.containers.list(all=True)
        vpn_containers = [c for c in containers if c.name.startswith(settings.VPN_PREFIX)]
        VpnInstance.objects.filter(name__in=[v.name for v in vpn_containers]).delete()

        for c in vpn_containers:
            port = c.ports['5000/tcp'][0]['HostPort']
            ip_address = "127.0.0.1"
            logger.info(f'Create instance [{c.name}] with address {ip_address}:{port}')
            instance = VpnInstance.objects.create(
                ip_address=ip_address,
                port=port,
                name=c.name,
                country=random.choice(list(countries)),
                is_online=False

            )
            for p in protocols:
                instance.protocols.add(p)

            instance.save()