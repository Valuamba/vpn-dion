from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.bot_locale import BotLocale
from ...types import Response


def _get_kwargs(
    alias: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/bot-locale/{alias}/".format(client.base_url, alias=alias)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[BotLocale]:
    if response.status_code == 200:
        response_200 = BotLocale.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[BotLocale]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    alias: str,
    *,
    client: Client,
) -> Response[BotLocale]:
    """
    Args:
        alias (str):

    Returns:
        Response[BotLocale]
    """

    kwargs = _get_kwargs(
        alias=alias,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    alias: str,
    *,
    client: Client,
) -> Optional[BotLocale]:
    """
    Args:
        alias (str):

    Returns:
        Response[BotLocale]
    """

    return sync_detailed(
        alias=alias,
        client=client,
    ).parsed


async def asyncio_detailed(
    alias: str,
    *,
    client: Client,
) -> Response[BotLocale]:
    """
    Args:
        alias (str):

    Returns:
        Response[BotLocale]
    """

    kwargs = _get_kwargs(
        alias=alias,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    alias: str,
    *,
    client: Client,
) -> Optional[BotLocale]:
    """
    Args:
        alias (str):

    Returns:
        Response[BotLocale]
    """

    return (
        await asyncio_detailed(
            alias=alias,
            client=client,
        )
    ).parsed
