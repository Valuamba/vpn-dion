from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.vpn_item import VpnItem
from ...types import Response


def _get_kwargs(
    pkid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/vpn-item/{pkid}/".format(client.base_url, pkid=pkid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[VpnItem]:
    if response.status_code == 200:
        response_200 = VpnItem.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[VpnItem]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pkid: str,
    *,
    client: Client,
) -> Response[VpnItem]:
    """
    Args:
        pkid (str):

    Returns:
        Response[VpnItem]
    """

    kwargs = _get_kwargs(
        pkid=pkid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pkid: str,
    *,
    client: Client,
) -> Optional[VpnItem]:
    """
    Args:
        pkid (str):

    Returns:
        Response[VpnItem]
    """

    return sync_detailed(
        pkid=pkid,
        client=client,
    ).parsed


async def asyncio_detailed(
    pkid: str,
    *,
    client: Client,
) -> Response[VpnItem]:
    """
    Args:
        pkid (str):

    Returns:
        Response[VpnItem]
    """

    kwargs = _get_kwargs(
        pkid=pkid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pkid: str,
    *,
    client: Client,
) -> Optional[VpnItem]:
    """
    Args:
        pkid (str):

    Returns:
        Response[VpnItem]
    """

    return (
        await asyncio_detailed(
            pkid=pkid,
            client=client,
        )
    ).parsed
