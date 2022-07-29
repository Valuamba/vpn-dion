import logging
from typing import Callable, Any, Awaitable, Optional, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat, User


class ACLMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user: Optional[User] = data.get("event_from_user")
        vpn_client = data.get("vpn_client")

        user = await vpn_client.post("bot_user/create", data={
            "user_id": user.id,
            "user_name": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name
        })

        data["user_db"] = user

        return await handler(event, data)
