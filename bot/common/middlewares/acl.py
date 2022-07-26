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
        chat: Optional[Chat] = data.get("event_chat")

        bot: Bot = data.get("bot")

        # if user and chat and chat.type == 'private':
        #     if not (user_db := await UserModel.find_one(UserModel.id == user.id)):
        #         role = UserRoles.new
        #         if str(user.id) in Config.ADMIN_ID:
        #             role = UserRoles.admin
        #         user_db = await UserModel(id=user.id, role=role, language_code=user.language_code,
        #                                   profile_name=user.full_name, nikname=user.username).create()
        #         await notify_new_user(user, bot)
        #         await update_user_commands(bot, user_db)
        #     elif user.full_name != user_db.full_name or user.username != user_db.nikname:
        #         user_db.nikname = user.username
        #         user_db.full_name = user.full_name
        #         await user_db.save()
        #
        #     data["user"] = user_db
        state = await data['state'].get_state()
        # logging.info(f"User [%s] state [%s]" % (data["user"].id, state))

        return await handler(event, data)
