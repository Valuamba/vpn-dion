# from aiogram import types, Bot
# from aiogram.exceptions import TelegramBadRequest
# from aiogram.types import BotCommandScopeChat
#
#
# async def set_user_commands(bot: Bot, user_id):
#     await bot.set_my_commands(
#         [
#             types.BotCommand(command="add_check", description="Добавить чек"),
#             types.BotCommand(command="profile", description="Профиль"),
#         ],
#         BotCommandScopeChat(chat_id=user_id)
#     )
#
#
# async def set_commands(bot: Bot) -> None:
#     users = await UserModel.find().to_list()
#     for user in users:
#         await update_user_commands(bot, user)
#
#
# async def update_user_commands(bot: Bot, user: UserModel):
#     try:
#         if user.role == UserRoles.user:
#             await set_auth_user_commands(bot, user.id)
#         elif user.role == UserRoles.manager:
#             await set_dispatcher_user_commands(bot, user.id)
#         elif user.role == UserRoles.admin:
#             await set_admin_user_commands(bot, user.id)
#     except TelegramBadRequest:
#         print(f'Chat {user.id}')
