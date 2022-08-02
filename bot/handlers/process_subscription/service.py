import decimal
import json

import httpx
from vpn_api_client.models import VpnDeviceTariff, VpnSubscription, VpnSubscriptionStatus, VpnSubscriptionVpnItemsItem, \
    CreateVpnItem

from common.gateways.vpn_rest_client import VpnRestClient
from handlers.process_subscription import Fields, DeviceFields
from handlers.process_subscription.helpers import get_tariff_str, get_device_configuration, get_result_price
from vpn_api_client.api.api import list_vpn_protocols, list_vpn_countrys, retrieve_vpn_device_tariff, create_vpn_subscription, \
    multiple_create_vpn_item, destroy_vpn_subscription

from vpn_api_client.types import Response


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
        if response.status_code == 201:
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

    price_per_month = float(tariff.duration_data.amount)
    duration = tariff.duration_data.month_duration
    devices_discount = tariff.discount_percentage
    devices_number = tariff.devices_number
    devcies = data.get(Fields.Devices, [])

    tariff_str = get_tariff_str(duration, devices_number,
                                price_per_month * devices_number,
                                tariff.duration_data.currency,
                                devices_discount)

    total_price = 0.0
    price_without_discounts = price_per_month * devices_number * duration

    devices_info = []
    for idx in range(devices_number):
        device = devcies[idx] if idx < len(devcies) else {
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

        devices_info.append(
            get_device_configuration(idx, country, protocol, device_price, tariff.duration_data.currency)
        )

    total_price = total_price * (100 - tariff.discount_percentage) / 100 * duration
    devices_str = '\n\n'.join(devices_info)

    form = f'''
    ⚖️ Выбранный тариф:

{tariff_str}

⚙️ Конфигурации устройств:

{devices_str}


{get_result_price(total_price, price_without_discounts, tariff.duration_data.currency)}
    '''

    return form