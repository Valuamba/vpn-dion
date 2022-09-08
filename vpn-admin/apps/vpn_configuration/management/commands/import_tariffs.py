import json
import logging
import os

from django.conf import settings
from django.core.management import BaseCommand
from djmoney.money import Money

from apps.bot_locale.models import MessageLocale
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_protocol.models import VpnProtocol, VpnProtocolType

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        dur_price_one = VpnDurationPrice.objects.create(month_duration=1, price=Money(290, 'RUB'))
        dur_price_six = VpnDurationPrice.objects.create(month_duration=6, price=Money(890, 'RUB'))
        dur_price_twelve = VpnDurationPrice.objects.create(month_duration=12, price=Money(1490, 'RUB'))

        VpnDeviceTariff.objects.create(duration=dur_price_one, devices_number=1,
                                       operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=0
                                       )
        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=1,
                                       operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=5
                                       )
        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=1,
                                       operation=VpnDeviceTariff.OperationType.EQUAL,
                                       discount_percentage=10
                                       )

        VpnDeviceTariff.objects.create(duration=dur_price_one, devices_number=2, operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=15)
        VpnDeviceTariff.objects.create(duration=dur_price_one, devices_number=3, operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=20)
        VpnDeviceTariff.objects.create(duration=dur_price_one, devices_number=4, operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL, discount_percentage=30)

        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=2,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=20)
        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=3,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=25)
        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=4, operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL,discount_percentage=35)

        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=2,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=25)
        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=3,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=30)
        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=4,operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL,discount_percentage=50)