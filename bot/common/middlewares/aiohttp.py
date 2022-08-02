import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.client.session import aiohttp
from aiogram.types import TelegramObject
from vpn_api_client import AuthenticatedClient

from common.gateways.vpn_rest_client import VpnRestClient
from config import Config

logger = logging.getLogger(__name__)


class AioHttpMiddleware(BaseMiddleware):

    def __init__(self):
        pass
        # self.vpn_client = VpnRestClient(Config.VPN_REST, Config.VPN_BEARER_TOKEN)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        # async with VpnRestClient(Config.VPN_REST, Config.VPN_BEARER_TOKEN) as session:
        client = AuthenticatedClient(token=Config.VPN_BEARER_TOKEN, base_url=Config.VPN_REST, verify_ssl=False,
                                     timeout=30
                                     )
        data["vpn_client"] = client
        await handler(event, data)
        # async with aiohttp.ClientSession() as session:
        #     data["aiohttp"] = session
        #     await handler(event, data)