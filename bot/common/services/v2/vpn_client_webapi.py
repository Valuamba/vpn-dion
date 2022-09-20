import json
from typing import List

from common.services.v2.types import VpnCountry, CreateSubscriptionDto, SubscriptionDetailsDto, VpnCountryList, \
    VpnDeviceTariff, VpnDeviceTariffList
from common.services.vpn_abstractions import send_get, send_post_v2, send_get_v2


async def get_available_countries(vpn_client) -> List[VpnCountry]:
    result = await send_get_v2(vpn_client, 'vpn-country/available')
    countries_root = VpnCountryList.parse_raw(result.content)
    return countries_root.__root__


async def create_single_device_subscription(*, user_id: int, tariff_id: int, country_id: int, vpn_client) -> CreateSubscriptionDto:
    result =await send_post_v2(vpn_client, 'vpn-subscription/single-device-create', json={
        'user_id': user_id,
        'tariff_id': tariff_id,
        'country_id': country_id
    })
    return json.loads(result.content, object_hook=lambda d: CreateSubscriptionDto(**d))


async def get_subscription_details(*, subscription_id, vpn_client) -> SubscriptionDetailsDto:
    result = await send_get_v2(vpn_client, f'vpn-subscription/details/{subscription_id}')
    return SubscriptionDetailsDto.parse_raw(result.content)


async def get_one_device_tariff(*, vpn_client) -> List[VpnDeviceTariff]:
    result = await send_get_v2(vpn_client, f'vpn-subscription/one-device-tariffs')
    tariffs_root = VpnDeviceTariffList.parse_raw(result.content)
    return tariffs_root.__root__
