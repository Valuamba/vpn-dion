import decimal
import json
import logging

from vpn_api_client import AuthenticatedClient
from vpn_api_client.models import VpnDeviceTariff, VpnSubscription, VpnSubscriptionStatus, VpnSubscriptionVpnItemsItem, \
    CreateVpnItem

from common.gateways.vpn_rest_client import VpnRestClient
from common.morph import get_morph
from common.services.vpn_client_webapi import send_post, send_get
from config import Config
from handlers.process_subscription import Fields, DeviceFields
from vpn_api_client.api.api import list_vpn_protocols, list_vpn_countrys
# from vpn_api_client.vpn_api_client import AuthenticatedClient
# from vpn_api_client.vpn_api_client.api.api import retrieve_message_locale
from common.services.vpn_client_webapi import gettext

logger = logging.getLogger(__name__)


async def create_subscription(data, user_id, vpn_client):
    tariff_id = data[Fields.SelectedSubscriptionOfferPkid]
    devices = data[Fields.Devices]

    subscription_request = {
        "tariff_id": tariff_id,
        "user_id": user_id,
        "devices": [{ "protocol_id": d[DeviceFields.SelectedProtocolPk], "country_id": d[DeviceFields.SelectedCountryPk] } for d in devices]
    }

    response = await send_post(vpn_client, 'subscription/create-subscription', json=subscription_request)

    return response.parsed


async def get_subscription(vpn_client, subscription_id):
    return (await send_get(vpn_client, f'vpn-subscription/{subscription_id}/')).parsed


async def get_devices_form_data(data, tariff: VpnDeviceTariff, vpn_client):
    countries = await list_vpn_countrys.asyncio(client=vpn_client)
    protocols = await list_vpn_protocols.asyncio(client=vpn_client)
    devices = data.get(Fields.Devices, [])

    price_per_month = float(tariff.duration_data.amount)
    devices_number = tariff.devices_number

    total_price = 0.0

    device_template = await gettext("deviceDetails")
    devices_info = []
    for idx in range(devices_number):
        device = devices[idx] if idx < len(devices) else {
            DeviceFields.DeviceIndex: idx,
            DeviceFields.SelectedProtocolPk: None,
            DeviceFields.SelectedCountryPk: None
        }
        country = None
        protocol = None
        if device[DeviceFields.SelectedCountryPk]:
            country = next(c for c in countries if c.pkid == device[DeviceFields.SelectedCountryPk])

        if device[DeviceFields.SelectedProtocolPk]:
            protocol = next(p for p in protocols if p.pkid == device[DeviceFields.SelectedProtocolPk])

        device_price = None
        if device[DeviceFields.SelectedCountryPk] and device[DeviceFields.SelectedProtocolPk]:
            device_price = price_per_month * (100 - country.discount_percentage) / 100
            total_price += device_price

        device_str = device_template.format(
            id=idx + 1,
            country=(country.country if country else '<i>введите страну</i>'),
            protocol=(protocol.protocol if protocol else '<i>введите протокол</i>'),
            device_price=(device_price if device_price else 'xxxx'),
            curr=tariff.duration_data.currency
        )
        devices_info.append(device_str)

    payment_request = {
        'duration_tariff_id': tariff.pkid,
        'devices': [{
            'country_id': d['selected_country_pk'],
            'protocol_id': d['selected_protocol_pk']
        } for d in devices if None not in d.values()]
    }

    devices_str = '\n'.join(devices_info)

    form = (await gettext("deviceConfiguration")).format(
        month_c=tariff.duration_data.month_duration,
        month_loc=get_morph('месяц', tariff.duration_data.month_duration),
        device_c=tariff.devices_number,
        device_loc=get_morph('устройство', tariff.devices_number),
        price=tariff.discounted_price,
        curr=tariff.duration_data.currency,
        discount=tariff.total_discount,
        devices_config=devices_str,
        result_price=tariff.discounted_price,
        initial_price=tariff.initial_price,
    )

    return form
