import decimal

from apps.vpn_order.models import VpnCountry
from apps.vpn_tariffs.models import VpnDeviceTariff
from lib.morph import get_morph


def get_tariff(tariff_id) -> VpnDeviceTariff:
    return VpnDeviceTariff.objects.get(pkid=tariff_id)


def calculate_device_discount(country_id: int) -> decimal.Decimal:
    country = VpnCountry.objects.get(pkid=country_id)
    country_discount = decimal.Decimal((100 - country.discount_percentage) / 100)
    return country_discount


def calculate_discounted_price(tariff: VpnDeviceTariff, promo_code_discount: int = 0):
    discount = decimal.Decimal((100 - (tariff.discount_percentage + promo_code_discount)) / 100)

    discounted_price = tariff.duration_data.amount * tariff.devices_number * discount

    discount_percentage = round(100 - ((discounted_price * 100) / tariff.initial_price))
    return discount_percentage, round(discounted_price)


def calculate_discounted_price_with_devices(tariff_id: int, promo_code_discount=0, devices=None):
    if devices is None:
        devices = []
    tariff = get_tariff(tariff_id)
    discount = decimal.Decimal((100 - (tariff.discount_percentage + promo_code_discount)) / 100)

    duration_price = decimal.Decimal(0.0)

    if len(devices) > tariff.devices_number and \
            not tariff.operation == VpnDeviceTariff.OperationType.GREATER_THAN_OR_EQUAL:
        raise Exception(
            f'Devices exceed available max number {tariff.devices_number} with operation {tariff.operation}'
            )

    if len(devices) < tariff.devices_number:
        raise Exception(f'Amount of devices is less then it must be in selected tariff {tariff.devices_number}')

    for device in devices:
        device_discount = calculate_device_discount(device['country_id'])
        duration_price += tariff.duration_data.amount * device_discount

    discounted_price = duration_price * discount

    discount_percentage = round(100 - ((discounted_price * 100) / tariff.initial_price))
    return discount_percentage, round(discounted_price)


def get_tariffs_details() -> []:
    tariffs = VpnDeviceTariff.objects.all().order_by('devices_number')
    tariffs_data = []
    for tariff in tariffs:
        discount_percentage, discounted_price = calculate_discounted_price(tariff)
        tariffs_data.append({
            'tariff_id': tariff.pkid,
            'month_duration': tariff.duration.month_duration,
            'month_loc': get_morph('месяц', tariff.duration.month_duration),
            'devices_number': tariff.devices_number,
            'devices_loc': get_morph('устройство', tariff.devices_number),
            'price': discounted_price,
            'currency': "RUB",
            'discount': discount_percentage
        })

    return tariffs_data
