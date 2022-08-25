import logging
from typing import Callable, Any, Awaitable, Optional, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat, User
# from vpn_api_client.api.api import list_vpn_items, create_bot_user, retrieve_bot_user
# from vpn_api_client.models import BotUser

from common.services.vpn_client_webapi import create_user
from common.set_commands import set_commands, update_user_commands


class ACLMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user: Optional[User] = data.get("event_from_user")
        vpn_client = data.get("vpn_client")

        # if not (bot_user := await retrieve_bot_user.asyncio(str(user.id), client=vpn_client)):
        #     referral_value=None
        #     if event.message:
        #         args = event.message.md_text.split(" ")[1:]
        #         if len(args) == 1 and args[0].startswith('ref'):
        #             referral_value = args[0]
        #
        #     bot_user = await create_user(vpn_client, user.id, str(user.username or ''), str(user.first_name or ''), str(user.last_name or ''), referral_value)
        #     await update_user_commands(data['bot'], user.id)
        #
        # if isinstance(bot_user, BotUser):
        #     data["user_db"] = bot_user.__dict__

        return await handler(event, data)
