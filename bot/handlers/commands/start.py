from aiogram import Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.menu import view as menuView, MenuStatesGroup


async def command_info(ctx: Message, bot: Bot, state: FSMContext, vpn_client):
    await state.clear()
    await menuView.fsmPipeline.move_to(ctx, bot, state, moved_state=MenuStatesGroup.Menu, vpn_client=vpn_client)


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="start")
    menuView.setup()
    menuView.fsmPipeline.build(dp)
