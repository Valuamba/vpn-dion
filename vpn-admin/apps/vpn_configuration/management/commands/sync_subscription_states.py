import logging
import time
from datetime import datetime

from django.core.management import BaseCommand

from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            try:
                subscriptions = VpnSubscription.objects.filter(subscription_end__lt=datetime.today(),
                                                               state=SubscriptionPaymentStatus.PAID_SUCCESSFULLY)

                for subscription in subscriptions:
                    for vpn_item in subscription.vpn_items:
                        logger.info(f'Remove VPN item {vpn_item.config_name}')
                        vpn_item.instance.client.remove_client(vpn_item.config_name)
                    subscriptions.status = SubscriptionPaymentStatus.OUTDATED
                    subscriptions.save()
            except Exception as e:
                logger.error(f'Error message: {str(e)}')

            time.sleep(30)