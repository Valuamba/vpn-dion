import pprint
import uuid

from django.core.management import BaseCommand
from django.utils import timezone
from djmoney.money import Money

from apps.bot_users.models import BotUser, ReferralItem
import random

from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus

#  python manage.py mock_referral_sub --owner=395040322
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--owner', type=int)

    def handle(self, *args, **kwargs):
        owner_id = kwargs['owner']

        owner = BotUser.objects.get(user_id=owner_id)

        ref_user_id = random.randrange(10000000, 70000000)
        referral_user = BotUser.objects.create(user_id=ref_user_id, referral_value=uuid.uuid4().__str__())

        ReferralItem.objects.create(referral_owner=owner, referred_user=referral_user)
        Money(amount=14342, currency='RUB')
        subscription = VpnSubscription.objects.create(
            user=referral_user,
            status=SubscriptionPaymentStatus.PAID_SUCCESSFULLY,
            subscription_end=timezone.now()
        )

