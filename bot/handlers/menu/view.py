from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from common.services.vpn_client_webapi import gettext as _
from handlers import account_subscriptions
from handlers.account_subscriptions import AccountSubscriptionsStateGroup
from handlers.menu import StateF
from handlers.process_subscription import view_tariff as process_view, ProcessSubscriptionStateGroup
from handlers.menu.keyboard import InlineM, MenuCD, MenuButtonType
from utils.fsm.fsm_utility import send_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from handlers.menu import utility_menu_commands
from handlers.account_subscriptions import view as account_subscriptions

fsmPipeline = FSMPipeline()


async def menu_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    await dialog_info(ctx, bot, state, text=await _("startText"),
                      reply_markup=await InlineM.get_menu_keyboard())


async def menu_handler(ctx: CallbackQuery, callback_data: MenuCD, bot: Bot, state: FSMContext, vpn_client):
    if callback_data.type == MenuButtonType.AVAILABLE_LOCATIONS:
        await fsmPipeline.move_to(ctx, bot, state, StateF.AvailableLocations, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.USER_SUBSCRIPTIONS:
        await fsmPipeline.move_to(ctx, bot, state, AccountSubscriptionsStateGroup.AllUserSubscriptions, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.HELP:
        await fsmPipeline.move_to(ctx, bot, state, StateF.Help, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.REFERRAL:
        pass
    elif callback_data.type == MenuButtonType.SUBSCRIBE:
        await fsmPipeline.move_to(ctx, bot, state, ProcessSubscriptionStateGroup.SelectTariff, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.INFO_ABOUT_VPN:
        await fsmPipeline.move_to(ctx, bot, state, StateF.About, vpn_client=vpn_client)


async def to_menu(ctx, bot, state, vpn_client):
    await fsmPipeline.move_to(ctx, bot, state, StateF.Menu, vpn_client=vpn_client)


def setup():

    prev_menu = (NavCD.filter(F.type==NavType.BACK), to_menu)
    process_view.setup(prev_menu)
    account_subscriptions.setup(prev_menu)
    utility_menu_commands.setup(prev_menu)

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.Menu, information=menu_info, handler=menu_handler,
                         filters=[MenuCD.filter()]),
        utility_menu_commands.fsmPipeline,
        process_view.fsmPipeline,
        account_subscriptions.fsmPipeline
    ])