from urllib.parse import urljoin

from common.services.vpn_client_webapi import send_get
from config import Config


async def get_all_user_subscriptions(user_id, vpn_client):
    response = await send_get(vpn_client, f'subscription/user-subscriptions/{user_id}/')
    user_subscriptions = response.parsed
    return user_subscriptions


async def get_all_subscription_devices(subscription_id, vpn_client):
    response = await send_get(vpn_client, f'vpn-items/subscription-vpn/{subscription_id}/')
    subscription_devices = response.parsed
    return subscription_devices


async def get_device_vpn_settings(device_id, vpn_client):
    response = await send_get(vpn_client, f'vpn-item/{device_id}/')
    vpn_item = response.parsed
    return vpn_item


def get_device_qrcode(device_id):
    return urljoin(Config.VPN_REST_HTTPS, f'api/v1/vpn-items/qrcode/{device_id}/')
