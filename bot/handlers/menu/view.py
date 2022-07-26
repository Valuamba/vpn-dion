from typing import Any

from aiogram import Dispatcher, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from handlers.menu import StateF
from handlers.process_subscription import view as process_view, ProcessSubscriptionStateGroup
from handlers.menu.keyboard import InlineM, MenuCD, MenuButtonType
from utils.fsm.fsm_utility import send_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse

fsmPipeline = FSMPipeline()


async def menu_info(ctx: Any, bot: Bot, state: FSMContext):
    await dialog_info(ctx, bot, state, text="Здравтсвуйте это приветственный текст",
                      reply_markup=InlineM.get_menu_keyboard())


async def menu_handler(ctx: CallbackQuery, callback_data: MenuCD, bot: Bot, state: FSMContext):
    if callback_data.type == MenuButtonType.AVAILABLE_LOCATIONS:
        pass
    elif callback_data.type == MenuButtonType.HELP:
        pass
    elif callback_data.type == MenuButtonType.REFERRAL:
        pass
    elif callback_data.type == MenuButtonType.SUBSCRIBE:
        await fsmPipeline.move_to(ctx, bot, state, ProcessSubscriptionStateGroup.SelectTariff)
    elif callback_data.type == MenuButtonType.INFO_ABOUT_VPN:
        pass


def setup():

    process_view.setup()

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.Menu, information=menu_info, handler=menu_handler,
                         filters=[MenuCD.filter()]),
        process_view.fsmPipeline
    ])