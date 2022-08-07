from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.update_vpn_subscription import UpdateVpnSubscription
from ...types import Response


def _get_kwargs(
    pkid: str,
    *,
    client: Client,
    form_data: UpdateVpnSubscription,
    multipart_data: UpdateVpnSubscription,
    json_body: UpdateVpnSubscription,
) -> Dict[str, Any]:
    url = "{}/api/v1/vpn-subscription/{pkid}/".format(client.base_url, pkid=pkid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UpdateVpnSubscription]:
    if response.status_code == 200:
        response_200 = UpdateVpnSubscription.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UpdateVpnSubscription]:
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
    form_data: UpdateVpnSubscription,
    multipart_data: UpdateVpnSubscription,
    json_body: UpdateVpnSubscription,
) -> Response[UpdateVpnSubscription]:
    """
    Args:
        pkid (str):
        multipart_data (UpdateVpnSubscription):
        json_body (UpdateVpnSubscription):

    Returns:
        Response[UpdateVpnSubscription]
    """

    kwargs = _get_kwargs(
        pkid=pkid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
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
    form_data: UpdateVpnSubscription,
    multipart_data: UpdateVpnSubscription,
    json_body: UpdateVpnSubscription,
) -> Optional[UpdateVpnSubscription]:
    """
    Args:
        pkid (str):
        multipart_data (UpdateVpnSubscription):
        json_body (UpdateVpnSubscription):

    Returns:
        Response[UpdateVpnSubscription]
    """

    return sync_detailed(
        pkid=pkid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    pkid: str,
    *,
    client: Client,
    form_data: UpdateVpnSubscription,
    multipart_data: UpdateVpnSubscription,
    json_body: UpdateVpnSubscription,
) -> Response[UpdateVpnSubscription]:
    """
    Args:
        pkid (str):
        multipart_data (UpdateVpnSubscription):
        json_body (UpdateVpnSubscription):

    Returns:
        Response[UpdateVpnSubscription]
    """

    kwargs = _get_kwargs(
        pkid=pkid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pkid: str,
    *,
    client: Client,
    form_data: UpdateVpnSubscription,
    multipart_data: UpdateVpnSubscription,
    json_body: UpdateVpnSubscription,
) -> Optional[UpdateVpnSubscription]:
    """
    Args:
        pkid (str):
        multipart_data (UpdateVpnSubscription):
        json_body (UpdateVpnSubscription):

    Returns:
        Response[UpdateVpnSubscription]
    """

    return (
        await asyncio_detailed(
            pkid=pkid,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed