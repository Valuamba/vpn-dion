import logging

import httpx

from common.services.vpn_client import AuthenticatedClient
from common.services.vpn_types import Response
# from vpn_api_client import AuthenticatedClient
# from vpn_api_client.api.api import retrieve_message_locale
# from vpn_api_client.types import Response

from config import Config

logger = logging.getLogger(__name__)


def _parse_response(*, response: httpx.Response):
    response_201 = ''
    if len(response.content) > 0:
        response_201 = response.json()

    return response_201


async def send_get(vpn_client, method):
    url = "{}/api/v1/{}".format(vpn_client.base_url, method)

    kwargs = {
        "method": "get",
        "url": url,
        "headers": vpn_client.get_headers(),
        "cookies": vpn_client.get_cookies(),
        "timeout": vpn_client.get_timeout(),
    }

    async with httpx.AsyncClient(verify=vpn_client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

        if response.status_code not in [200, 201]:
            raise Exception(response.text)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(response=response),
        )


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

    async with httpx.AsyncClient(verify=vpn_client.verify_ssl) as _client:
        response = await _client.request(**body)

        if response.status_code not in [200, 201]:
            raise Exception(response.text)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(response=response),
        )


async def gettext(alias: str) -> str:
    logger.info(f'Get locale: {alias}')
    client = AuthenticatedClient(token=Config.VPN_BEARER_TOKEN, base_url=Config.VPN_REST, verify_ssl=False,
                                 timeout=30
                                 )
    return (await send_get(client, f'bot_locale/locale/{alias}')).parsed


async def get_locales(*aliases) -> []:
    logger.info(f'Get locale: {", ".join(aliases)}')
    client = AuthenticatedClient(token=Config.VPN_BEARER_TOKEN, base_url=Config.VPN_REST, verify_ssl=False,
                                 timeout=30
                                 )
    alias_data = {
        'aliases': aliases
    }
    locales = (await send_post(client, 'bot_locale/bulk-locale', json=alias_data)).parsed
    return locales


async def create_user(vpn_client, user_id, user_name, first_name, last_name, referral_value=None):
    result = await send_post(vpn_client, 'bot_user/create', json={
        "user_id": user_id,
        "user_name": user_name,
        "first_name": first_name,
        "last_name": last_name,
        "referral_value": referral_value
    })

    return result.parsed


async def update_user(vpn_client, **update_user):
    result = await send_post(vpn_client, f'bot_user/update/{update_user["user_id"]}', json_body={
        "user_name": update_user["user_name"],
        "first_name": update_user["first_name"],
        "last_name": update_user["last_name"],
        "referral_value": update_user["referral_value"]
    })

    return result.parsed


async def activate_invited_user_subscription(user_id, vpn_client, days_duration):
    result = await send_post(vpn_client, f'subscription/invited-user-subscription', json={
        'user_id': user_id,
        'days_duration': days_duration
    })
    return result.parsed


async def add_feedback_message(user_id, message_id, text, vpn_client):
    result = await send_post(vpn_client, f'feedback/message', json={
        'user_id': user_id,
        'message_id': message_id,
        'text': text
    })

    return result.parsed

async def get_user(vpn_client, user_id):
    try:
        result = await send_get(vpn_client, f'bot_user/{user_id}/')
        return result.parsed
    except Exception:
        return None