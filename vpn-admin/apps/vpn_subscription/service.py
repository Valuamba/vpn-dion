import logging
import traceback
import uuid
from typing import List

from dateutil.relativedelta import relativedelta
from django.db import transaction
from django.utils import timezone
from djmoney.money import Money

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.selectors import get_tariff, calculate_discounted_price_with_devices
from apps.vpn_instance.models import VpnInstance
from apps.vpn_item.models import VpnItem
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription, SubscriptionPaymentStatus, SubReminderState
from apps.vpn_subscription.selectors import get_default_country, get_default_protocol, get_promo_code, \
    get_available_instance, get_subscription_by_uuid
from lib.freekassa import get_freekassa_checkout

logger = logging.getLogger(__name__)


def create_payment_provider_link(*, subscription_id: uuid, state: str, promo_code: str = None, payment_provider='Freekassa') -> str:
    if payment_provider == 'Freekassa':
        subscription = get_subscription_by_uuid(subscription_id)
        freekassa_url = get_freekassa_checkout(
            amount=subscription.price.amount,
            currency=subscription.price.currency,
            subscription_id=subscription.pkid,
            us_state=state,
            us_promocode= promo_code
        )
        return freekassa_url

    raise Exception('Unrecognized payment provider')


@transaction.atomic()
def create_subscription(
        *,
        user_id: int,
        tariff_id: int,
        devices: [],
        promo_code: str = None,
        **args
) -> VpnSubscription:
    promo_code_obj = None
    promo_code_discount = 0
    if promo_code:
        promo_code_obj = get_promo_code(promo_code=promo_code)
        promo_code_discount = promo_code_obj.discount

    tariff = get_tariff(tariff_id)

    currency = "RUB"
    discount, discounted_price = calculate_discounted_price_with_devices(tariff_id, promo_code_discount, devices)
    subscription_end = timezone.now() + relativedelta(months=tariff.duration.month_duration)

    subscription = VpnSubscription.objects.create(
        user_id=user_id,
        tariff_id=tariff_id,
        month_duration=tariff.duration.month_duration,
        devices_number=tariff.devices_number,
        is_referral=False,
        price=Money(amount=discounted_price, currency=currency),
        discount=discount,
        subscription_end=subscription_end,
        status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT,
        reminder_state=SubReminderState.SEVEN_DAYS_REMINDER
        # promo_code=promo_code_obj
    )

    vpn_items = []
    for device in devices:
        instance = get_available_instance(country_id=device['country_id'], protocol_id=device['protocol_id'])
        item = VpnItem(instance=instance, protocol_id=device['protocol_id'], vpn_subscription_id=subscription.pkid)
        vpn_items.append(item)

    VpnItem.objects.bulk_create(vpn_items)
    return subscription


@transaction.atomic
def create_vpn_items(*, country: VpnCountry, protocol: VpnProtocol, devices_number: int, subscription_id: int,
                     user_id: int):
    changed_items = []
    for i in range(devices_number):
        instance = VpnInstance.objects.filter(country=country, protocols=protocol, is_online=True).first()
        if not instance:
            raise Exception(f'There are no online instances with country: {country}')

        client_response = instance.client.create_client(user_id)

        item = VpnItem(instance=instance, protocol=protocol, vpn_subscription_id=subscription_id)
        item.public_key = client_response.public_key
        item.private_key = client_response.private_key
        item.address = client_response.address
        item.dns = client_response.dns
        item.preshared_key = client_response.preshared_key
        item.endpoint = client_response.endpoint
        item.allowed_ips = client_response.allowed_ips
        item.config_name = client_response.config_name
        item.save()
        logger.info(f'Create config for vpn item {item.pkid}')

        changed_items.append(item)

    return changed_items


@transaction.atomic
def create_trial_vpn_subscription(*, user_id: int) -> int:
    DEVICES_NUMBER = 1
    DAYS_DURATION = 7

    logger.info(f'Activate free subscription with {DAYS_DURATION} days for invited user {user_id}')

    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    devices_number = 1
    country = get_default_country()
    protocol = get_default_protocol()

    subscription_end = timezone.now() + relativedelta(days=DAYS_DURATION)

    if not country:
        raise Exception('Country was not found.')

    if not protocol:
        raise Exception('Protocol was not found.')

    changed_items = []
    try:
        subscription = VpnSubscription.objects.create(user_id=user_id,
                                                      status=SubscriptionPaymentStatus.PAID_SUCCESSFULLY,
                                                      devices_number=DEVICES_NUMBER, days_duration=DAYS_DURATION,
                                                      subscription_end=subscription_end, is_referral=True,
                                                      reminder_state=SubReminderState.SEVEN_DAYS_REMINDER
                                                      )
        changed_items = create_vpn_items(country=country, protocol=protocol, devices_number=devices_number,
                                         subscription_id=subscription.pkid, user_id=user_id
                                         )
        return subscription.pkid
    except Exception as e:
        for item in changed_items:
            item.instance.client.remove_client(item.config_name)
        logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')
        raise Exception(str(e))


@transaction.atomic
def fail_subscription(*, subscription_id: int):
    logger.info(f'Start failing subscription {subscription_id}')

    subscription: VpnSubscription = VpnSubscription.objects.get(pkid=subscription_id)
    vpn_items: List[VpnItem] = VpnItem.objects.filter(vpn_subscription_id=subscription_id)

    for item in vpn_items:
        logger.info(f'Remove VPN Item {item.pkid}, config_name: {item.config_name}')
        try:
            item.instance.client.remove_client(item.config_name)
        except Exception as e:
            item.status = VpnItem.Status.FAILED
            logger.error(f'Error: {str(e)}\nTrace: {traceback.format_exc()}')

        item.status = VpnItem.Status.REMOVED
        item.save()

    subscription.status = SubscriptionPaymentStatus.DEFECTIVE
    subscription.save()
