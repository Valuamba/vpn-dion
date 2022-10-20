import logging
import random
from typing import List

import docker
from django.core.management import BaseCommand
from django.conf import settings
from django.db import transaction
from django_countries.data import COUNTRIES
from django.utils import timezone
from apps.vpn_item.models import VpnItem
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.service import remove_outdated_subscriptions

class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        remove_outdated_subscriptions()
        