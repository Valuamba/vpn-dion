from aiogram import types, Bot
from aiogram.types import BotCommandScopeChat
from vpn_api_client import AuthenticatedClient
from vpn_api_client.api.api import list_bot_users

from config import Config


async def update_user_commands(bot: Bot, user_id):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Начало"),
        ],
        BotCommandScopeChat(chat_id=user_id)
    )


async def set_commands(bot: Bot) -> None:
    client = AuthenticatedClient(token=Config.VPN_BEARER_TOKEN, base_url=Config.VPN_REST, verify_ssl=False,
                                 timeout=30
                                 )
    users = await list_bot_users.asyncio(client=client)
    for user in users:
        await update_user_commands(bot, user.user_id)
