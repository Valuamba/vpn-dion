from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: Any,
    json_body: Any,
) -> Dict[str, Any]:
    url = "{}/api/v1/vpn_device_tariff/recalculate-payment-details".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: Any,
    json_body: Any,
) -> Response[Any]:
    """
    Args:
        multipart_data (Any):
        json_body (Any):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: Any,
    json_body: Any,
) -> Response[Any]:
    """
    Args:
        multipart_data (Any):
        json_body (Any):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
