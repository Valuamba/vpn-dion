import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.client.session import aiohttp
from aiogram.types import TelegramObject

from common.gateways.vpn_rest_client import VpnRestClient
from config import Config

logger = logging.getLogger(__name__)


class AioHttpMiddleware(BaseMiddleware):

    def __init__(self):
        self.vpn_client = VpnRestClient(Config.VPN_REST, Config.VPN_BEARER_TOKEN)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        # await create_vpn_subscription.asyncio(client=client,
        #                                       data=VpnSubscription(
        #                                           vpn_items=[],
        #                                           status=VpnSubscriptionStatus
        #                                       ))



        data["vpn_client"] = self.vpn_client
        await handler(event, data)
