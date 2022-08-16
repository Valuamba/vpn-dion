import logging
from typing import Callable, Any, Awaitable, Optional, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat, User
from vpn_api_client.api.api import list_vpn_items, create_bot_user, retrieve_bot_user
from vpn_api_client.models import BotUser

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

        if not (bot_user := await retrieve_bot_user.asyncio(str(user.id), client=vpn_client)):
            bot_user = BotUser(
                user_id=user.id,
                user_name=str(user.username or ''),
                first_name=str(user.first_name or ''),
                last_name=str(user.last_name or ''))
            bot_user = await create_bot_user.asyncio(client=vpn_client, form_data=bot_user, multipart_data=bot_user, json_body=bot_user)
            await update_user_commands(data['bot'], user.id)

        data["user_db"] = bot_user

        return await handler(event, data)
