import logging
import random
from typing import List

import docker
from django.core.management import BaseCommand
from django.conf import settings
from django.db import transaction
from django_countries.data import COUNTRIES

from apps.vpn_country.models import VpnCountry
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.service import fail_subscription, create_trial_vpn_subscription

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--owner', type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        owner_id = options['owner']
        days_duration = 7

        query = f"""
select s.* from public.vpn_subscriptions as s
inner join public.referral_items as r on s.user_id = r.referred_user_id
where s.days_duration = {days_duration} and r.referral_owner_id = {owner_id}
"""

        subscriptions: List[VpnSubscription] = VpnSubscription.objects.raw(query)

        for sub in subscriptions:
            fail_subscription(subscription_id=sub.pkid)
            create_trial_vpn_subscription(user_id=sub.user.user_id)




