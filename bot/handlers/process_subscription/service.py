import decimal
import json
import logging

import httpx
from vpn_api_client import AuthenticatedClient
from vpn_api_client.models import VpnDeviceTariff, VpnSubscription, VpnSubscriptionStatus, VpnSubscriptionVpnItemsItem, \
    CreateVpnItem

from common.gateways.vpn_rest_client import VpnRestClient
from config import Config
from handlers.process_subscription import Fields, DeviceFields
from vpn_api_client.api.api import list_vpn_protocols, list_vpn_countrys, retrieve_vpn_device_tariff, \
    create_vpn_subscription, \
    multiple_create_vpn_item, destroy_vpn_subscription, retrieve_message_locale
from vpn_api_client.types import Response
# from vpn_api_client.vpn_api_client import AuthenticatedClient
# from vpn_api_client.vpn_api_client.api.api import retrieve_message_locale
from handlers.process_subscription.helpers import get_morph

logger = logging.getLogger(__name__)


async def create_subscription(data, user_id, vpn_client):
    tariff_id = data[Fields.SelectedSubscriptionOfferPkid]
    devices = data[Fields.Devices]

    subscription = VpnSubscription(
        vpn_items=[],
        #waiting for
        status=VpnSubscriptionStatus.WAITING_FOR_PAYMENT,
        tariff=tariff_id,
        user=user_id,
        total_price='1000',
        discount='12'
    )

    new_subscription = await create_vpn_subscription.asyncio(client=vpn_client, form_data=subscription, multipart_data=subscription, json_body=subscription)

    vpn_items = []
    for d in devices:
        vpn_items.append(
            CreateVpnItem(
                vpn_subscription=new_subscription.pkid,
                protocol=d[DeviceFields.SelectedProtocolPk],
                instance=d[DeviceFields.SelectedCountryPk]
            ))

    json_data = json.dumps([item.to_dict() for item in vpn_items])
    response = await send_post(vpn_client, 'vpn-item/multiple/create/', json=json_data)
    if response.status_code != 201:
        await destroy_vpn_subscription.asyncio_detailed(pkid=str(new_subscription.pkid), client=vpn_client)

    return new_subscription.pkid


async def send_post(vpn_client, method, **kwargs):
    url = "{}/api/v1/{}".format(vpn_client.base_url, method)

    body = {
        "method": "post",
        "url": url,
        "headers": vpn_client.get_headers(),
        "cookies": vpn_client.get_cookies(),
        "timeout": vpn_client.get_timeout(),
        **kwargs
    }

    def _parse_response(*, response: httpx.Response):
        if response.status_code in [201, 200]:
            response_201 = response.json()

            return response_201
        return None

    async with httpx.AsyncClient(verify=vpn_client.verify_ssl) as _client:
        response = await _client.request(**body)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(response=response),
        )


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
            device_price=device_price,
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


async def gettext(alias: str) -> str:
    logger.info(f'Get locale: {alias}')
    client = AuthenticatedClient(token=Config.VPN_BEARER_TOKEN, base_url=Config.VPN_REST, verify_ssl=False,
                                 timeout=30
                                 )
    locale = await retrieve_message_locale.asyncio(alias, client=client)
    return locale.text