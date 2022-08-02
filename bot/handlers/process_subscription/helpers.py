from typing import Dict, List

from vpn_api_client.models import VpnDeviceTariff, VpnCountry, VpnProtocol

from common.models.subscription_offer import SubscriptionOfferDevicesType
from handlers.process_subscription import DeviceFields, Fields

MonthLocale = {
    1: 'месяц',
    2: 'месяца',
    3: 'месяца',
    4: 'месяца',
    5: 'месяцев',
    6: 'месяцев',
    7: 'месяцев',
    8: 'месяцев',
    9: 'месяцев',
    10: 'месяцев',
    11: 'месяцев',
    12: 'месяцев'
}


NumberEmoji = {
    1: '1️⃣',
    2: '2️⃣',
    3: '3️⃣',
    4: '4️⃣',
    5: '5️⃣',
    6: '6️⃣',
    7: '7️⃣',
    8: '8️⃣',
    9: '9️⃣',
    10: '🔟'

}
DeviceLocale = {
    SubscriptionOfferDevicesType.ONE: '1 устройство',
    SubscriptionOfferDevicesType.TWO: '2 устройства',
    SubscriptionOfferDevicesType.THREE: '3 устройства',
    SubscriptionOfferDevicesType.FOUR_OR_MORE: '4 и более',
}


CurrencyLocale = {
    'RUB': '₽'
}


def get_device_locale(device_count, price, discount, currency: str) -> str:
    return '%s устройство: %s %s (дешевле на %s)' % (device_count, price, CurrencyLocale[currency], str(discount) + '%')


def get_month_text(m_count):
    return '%s %s' % (m_count, "месяц(ев)")


def get_tariff_str(month_duration, devices_number, price, currency, discount):
    result_price = price * (100 - discount) / 100

    return f"🗓 {month_duration} месяц(ев) 📱{devices_number}: " \
           f"{result_price} {CurrencyLocale[currency]} (дешевле на {discount}%)"


def get_result_price(total_price, actually_price, currency):
    s = f"💳 К оплате: {total_price} {CurrencyLocale[currency]}"
    if total_price and total_price != 0:
        s += f" (без скидок {actually_price} {CurrencyLocale[currency]})"
    return s


def get_device_configuration(index, country: VpnCountry, protocol: VpnProtocol, device_price, currency):
    country_str = '<i>выберите страну</i>'
    wireguard_str = '<i>выберите протокол</i>'
    if country:
        country_str = f"🗺 {country.country}"
        if country.discount_percentage != 0:
            country_str += f" (дешевле на {country.discount_percentage}%)"

    if protocol:
        wireguard_str = protocol.protocol

    total_price_str = ''
    if protocol and country:
        total_price_str = f" — {device_price} {CurrencyLocale[currency]}"

    return f"{NumberEmoji[index + 1]} {country_str} · {wireguard_str}{total_price_str}"


def get_device_by_index(devices: [], index):
    return (device for device in devices if device.get(DeviceFields.DeviceIndex, None) == index)


def group_subscription_offers_by_month(subscriptions_offers: List[VpnDeviceTariff]) -> Dict[int, List[VpnDeviceTariff]]:
    grouped_subs: Dict[int, List[VpnDeviceTariff]] = {}

    for idx, offer in enumerate(subscriptions_offers):
        offers = grouped_subs.setdefault(offer.duration_data.month_duration, [])
        offers.append(subscriptions_offers[idx])

    return grouped_subs


def is_all_devices_meet_condition(devices: dict, devices_number: int) -> bool:
    if devices and len(devices) >= devices_number:
        for device in devices:
            if not is_device_configured(device):
                return False

        return True

    return False


def is_device_configured(device: dict):
    if device.get(DeviceFields.DeviceIndex, None) is not None \
            and device.get(DeviceFields.SelectedCountryPk, None) \
            and device.get(DeviceFields.SelectedProtocolPk, None):
        return True
    else:
        return False

