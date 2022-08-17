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
        wireguard = VpnProtocol.objects.create(protocol=VpnProtocolType.WIREGUARD)
        open_vpn = VpnProtocol.objects.create(protocol=VpnProtocolType.OPEN_VPN)

        dur_price_one = VpnDurationPrice.objects.create(month_duration=1, price=Money(300, 'RUB'))
        dur_price_three = VpnDurationPrice.objects.create(month_duration=3, price=Money(290, 'RUB'))
        dur_price_six = VpnDurationPrice.objects.create(month_duration=6, price=Money(600, 'RUB'))
        dur_price_twelve = VpnDurationPrice.objects.create(month_duration=12, price=Money(890, 'RUB'))

        VpnDeviceTariff.objects.create(duration=dur_price_three, devices_number=2, operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_three, devices_number=3, operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_three, devices_number=4, operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL, discount_percentage=13)

        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=2,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=3,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_six, devices_number=4, operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL,discount_percentage=13)

        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=2,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=3,operation=VpnDeviceTariff.OperationType.EQUAL, discount_percentage=13)
        VpnDeviceTariff.objects.create(duration=dur_price_twelve, devices_number=4,operation=VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL,discount_percentage=13)