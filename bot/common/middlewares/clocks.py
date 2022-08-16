from typing import Any, Optional, Callable, Awaitable, Dict

from aiogram import BaseMiddleware, types, Bot
from aiogram.dispatcher.event.handler import CallbackType
from aiogram.types import Chat, Message


class ClocksMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: types.TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        real_handler: CallbackType = data["handler"]

        chat: Optional[Chat] = data.get("event_chat")

        allow = hasattr(real_handler.callback, "clocks")

        bot: Bot = data['bot']

        if not allow:
            return await handler(event, data)

        msg: Optional[Message] = None
        if chat:
            msg = await bot.send_message(chat.id, "⏳")
            await bot.send_chat_action(chat.id, "typing")

        result = await handler(event, data)

        if msg:
            await msg.delete()

        return result
