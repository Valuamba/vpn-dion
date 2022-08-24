from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common.services.vpn_client_webapi import update_user
from handlers.menu import view as menuView, MenuStatesGroup


async def command_info(ctx: Message, bot: Bot, state: FSMContext, vpn_client):
    # if command.args and len(command.args) > 0 and command.args[0].startswith('ref'):
    #     await update_user(vpn_client, **{
    #         **user_db,
    #         'referral_value': command.args[0]
    #     })

    await state.clear()
    await menuView.fsmPipeline.move_to(ctx, bot, state, moved_state=MenuStatesGroup.Menu, vpn_client=vpn_client)


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="start")
    menuView.setup()
    menuView.fsmPipeline.build(dp)
