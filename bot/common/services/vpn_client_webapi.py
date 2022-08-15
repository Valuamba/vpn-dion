import logging

import httpx
from vpn_api_client import AuthenticatedClient
from vpn_api_client.api.api import retrieve_message_locale
from vpn_api_client.types import Response

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
    locale = await retrieve_message_locale.asyncio(alias, client=client)
    return locale.text


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