from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from handlers.menu import StateF
from handlers.process_subscription import view_tariff as process_view, ProcessSubscriptionStateGroup
from handlers.menu.keyboard import InlineM, MenuCD, MenuButtonType
from utils.fsm.fsm_utility import send_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse

fsmPipeline = FSMPipeline()


async def menu_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    await dialog_info(ctx, bot, state, text="Здравтсвуйте это приветственный текст",
                      reply_markup=InlineM.get_menu_keyboard())


async def menu_handler(ctx: CallbackQuery, callback_data: MenuCD, bot: Bot, state: FSMContext, vpn_client):
    if callback_data.type == MenuButtonType.AVAILABLE_LOCATIONS:
        pass
    elif callback_data.type == MenuButtonType.HELP:
        pass
    elif callback_data.type == MenuButtonType.REFERRAL:
        pass
    elif callback_data.type == MenuButtonType.SUBSCRIBE:
        await fsmPipeline.move_to(ctx, bot, state, ProcessSubscriptionStateGroup.SelectTariff, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.INFO_ABOUT_VPN:
        pass


async def to_menu(ctx, bot, state, vpn_client):
    await fsmPipeline.move_to(ctx, bot ,state, StateF.Menu, vpn_client=vpn_client)


def setup():

    process_view.setup((NavCD.filter(F.type==NavType.BACK), to_menu))

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.Menu, information=menu_info, handler=menu_handler,
                         filters=[MenuCD.filter()]),
        process_view.fsmPipeline
    ])