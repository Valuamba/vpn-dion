import logging
import httpx
from common.services.vpn_types import Response

logger = logging.getLogger(__name__)


def _parse_response(*, response: httpx.Response):
    response_201 = ''
    if len(response.content) > 0:
        response_201 = response.json()

    return response_201


async def send_get_v2(vpn_client, method):
    url = "{}/api/v2/{}".format(vpn_client.base_url, method)

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
            raise Exception(response.reason_phrase)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=None,
        )


async def send_post_v2(vpn_client, method, **kwargs):
    url = "{}/api/v2/{}".format(vpn_client.base_url, method)

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
            raise Exception(response.reason_phrase)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=None,
        )


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
            raise Exception(response.reason_phrase)

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
            raise Exception(response.reason_phrase)

        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(response=response),
        )

