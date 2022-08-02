from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.token_refresh import TokenRefresh
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Dict[str, Any]:
    url = "{}/api/v1/token/refresh/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[TokenRefresh]:
    if response.status_code == 201:
        response_201 = TokenRefresh.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[TokenRefresh]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Response[TokenRefresh]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        multipart_data (TokenRefresh):
        json_body (TokenRefresh):

    Returns:
        Response[TokenRefresh]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Optional[TokenRefresh]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        multipart_data (TokenRefresh):
        json_body (TokenRefresh):

    Returns:
        Response[TokenRefresh]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Response[TokenRefresh]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        multipart_data (TokenRefresh):
        json_body (TokenRefresh):

    Returns:
        Response[TokenRefresh]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    form_data: TokenRefresh,
    multipart_data: TokenRefresh,
    json_body: TokenRefresh,
) -> Optional[TokenRefresh]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        multipart_data (TokenRefresh):
        json_body (TokenRefresh):

    Returns:
        Response[TokenRefresh]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
