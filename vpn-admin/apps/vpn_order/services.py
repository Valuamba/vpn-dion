import io
import uuid
from configparser import ConfigParser

import qrcode
from dateutil.relativedelta import relativedelta
from django.db import transaction
from django.utils import timezone
from djmoney.money import Money

from apps.vpn_duration_tariff.selectors import get_tariff, \
    calculate_discounted_price_with_devices
from apps.vpn_instance.selectors import get_available_instance
from apps.vpn_order.models import VpnSubscription, VpnItem
from apps.vpn_order.selectors import get_promo_code, get_subscription_by_uuid, get_vpn_item
from apps.vpn_subscription.models import SubscriptionPaymentStatus
from lib.freekassa import get_freekassa_checkout


@transaction.atomic()
def create_subscription(
        *,
        user_id: int,
        tariff_id: int,
        promo_code: str,
        devices: [],
) -> VpnSubscription:
    promo_code_obj = get_promo_code(promo_code=promo_code)
    tariff = get_tariff(tariff_id)

    currency = "RUB"
    discount, discounted_price = calculate_discounted_price_with_devices(tariff_id, promo_code_obj.discount, devices)
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
        promo_code=promo_code_obj
    )

    vpn_items = []
    for device in devices:
        instance = get_available_instance(country_id=device['country_id'], protocol_id=device['protocol_id'])
        item = VpnItem(instance=instance, protocol_id=device['protocol_id'], vpn_subscription_id=subscription.pkid)
        vpn_items.append(item)

    VpnItem.objects.bulk_create(vpn_items)
    return subscription


def create_payment_provider_link(*, subscription_id: uuid, state: str, payment_provider='Freekassa') -> str:
    if payment_provider == 'Freekassa':
        subscription = get_subscription_by_uuid(subscription_id)
        freekassa_url = get_freekassa_checkout(
            amount=subscription.price.amount,
            currency=subscription.price.currency,
            subscription_id=subscription.pkid,
            us_state=state,
            us_promocode=subscription.promo_code.name
        )
        return freekassa_url

    raise Exception('Unrecognized payment provider')


def create_vpn_config_file(*, vpn_item_id: int):
    vpn_item = get_vpn_item(vpn_item_id=vpn_item_id)

    config = ConfigParser()
    config.optionxform = str
    interface_section = 'Interface'
    peer_section = 'Peer'
    config.add_section(interface_section)
    config.set(interface_section, "PrivateKey", vpn_item.private_key)
    config.set(interface_section, "Address", vpn_item.address)
    config.set(interface_section, "DNS", vpn_item.dns)

    config.add_section(peer_section)
    config.set(peer_section, "PublicKey", vpn_item.public_key)
    config.set(peer_section, "PresharedKey", vpn_item.preshared_key)
    config.set(peer_section, "Endpoint", vpn_item.endpoint)
    config.set(peer_section, "AllowedIPs", vpn_item.allowed_ips)

    with io.StringIO() as output:
        config.write(output)
        contents = output.getvalue()
        return contents


def generate_qr_code(vpn_item_id: int):
    qr_str = create_vpn_config_file(vpn_item_id=vpn_item_id)

    internal_image = qrcode.make(qr_str)
    file_like_image = io.BytesIO()
    internal_image.save(file_like_image, format="PNG")
    file_like_image.seek(0)

    return file_like_image
