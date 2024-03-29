import logging
from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from common.services.v2.vpn_client_webapi import get_one_device_tariff
from common.services.vpn_client_webapi import gettext as _, get_user_active_subscriptions
from handlers import account_subscriptions
from handlers.account_subscriptions import AccountSubscriptionsStateGroup
from handlers.bot_tariff import BotTariffGroup, Fields
from handlers.broadcast.states import BroadcastAdmin
from handlers.menu import StateF
# from handlers.process_subscription import view_tariff as process_view, ProcessSubscriptionStateGroup
from handlers.menu.keyboard import InlineM, MenuCD, MenuButtonType, FastVpnTariff
from utils.fsm.fsm_utility import send_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from handlers.menu import utility_menu_commands
from handlers.account_subscriptions import view as account_subscriptions
from handlers.feedback import view as feedback, FeedbackStateGroup
from handlers.referral import view as referral, ReferralStateGroup
from handlers.bot_tariff import view as bot_tariff
from handlers.reviews import view as reviews, ReviewsStateGroup
from handlers.broadcast import broadcast
from utils.fsm.window_utility import remove_window_message
from utils.update import get_user_id

fsmPipeline = FSMPipeline()
logger = logging.getLogger(__name__)


async def menu_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    tariffs = await get_one_device_tariff(vpn_client=vpn_client)
    subs = await get_user_active_subscriptions(get_user_id(ctx), vpn_client)
    if len(subs) > 0:
        text = await _("userWithActivatedSubscription")
    else:
        text = await _("startText")
    logger.info(f'User: {get_user_id(ctx)}. Info menu.')

    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_menu_keyboard(user_id=get_user_id(ctx), tariffs=tariffs))


async def menu_handler(ctx: CallbackQuery, callback_data: MenuCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler menu navigation {ctx.data}')
    if callback_data.type == MenuButtonType.AVAILABLE_LOCATIONS:
        await fsmPipeline.move_to(ctx, bot, state, StateF.AvailableLocations, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.USER_SUBSCRIPTIONS:
        await fsmPipeline.move_to(ctx, bot, state, AccountSubscriptionsStateGroup.AllUserSubscriptions, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.HELP:
        await fsmPipeline.move_to(ctx, bot, state, FeedbackStateGroup.WriteFeedBackMessage, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.REFERRAL:
        await fsmPipeline.move_to(ctx, bot, state, ReferralStateGroup.ReferralMenu, vpn_client=vpn_client)
    # elif callback_data.type == MenuButtonType.SUBSCRIBE:
    #     await fsmPipeline.move_to(ctx, bot, state, ProcessSubscriptionStateGroup.SelectTariff, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.INFO_ABOUT_VPN:
        await fsmPipeline.move_to(ctx, bot, state, StateF.About, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.BROADCAST:
        await fsmPipeline.move_to(ctx, bot, state, BroadcastAdmin.BROADCAST, vpn_client=vpn_client)
    elif callback_data.type == MenuButtonType.REVIEWS:
        await fsmPipeline.move_to(ctx, bot, state, ReviewsStateGroup.SeeReviews, vpn_client=vpn_client)


async def fast_vpn_tariff_handler(ctx: CallbackQuery, callback_data: FastVpnTariff, bot: Bot, state: FSMContext, vpn_client):
    await state.update_data({ Fields.SelectedTariffId: callback_data.tariff_id })
    await fsmPipeline.move_to(ctx, bot, state, BotTariffGroup.SelectCountry, vpn_client=vpn_client)


async def to_menu(ctx, bot: Bot, state, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler move to Menu sate.')
    await remove_window_message(ctx, bot, state)
    await fsmPipeline.move_to(ctx, bot, state, StateF.Menu, vpn_client=vpn_client)


def setup():

    prev_menu = (NavCD.filter(F.type==NavType.BACK), to_menu)
    # process_view.setup(prev_menu)
    account_subscriptions.setup(prev_menu)
    utility_menu_commands.setup(prev_menu)
    referral.setup(prev_menu)
    feedback.setup(prev_menu)
    broadcast.setup(prev_menu)
    bot_tariff.setup(prev_menu)
    reviews.setup(prev_menu)

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.Menu, information=menu_info, handler=menu_handler,
                         inline_navigation_handler=[
                             (FastVpnTariff.filter(), fast_vpn_tariff_handler)
                         ],
                         filters=[MenuCD.filter()]),
        feedback.fsmPipeline,
        utility_menu_commands.fsmPipeline,
        # process_view.fsmPipeline,
        account_subscriptions.fsmPipeline,
        referral.fsmPipeline,
        broadcast.fsmPipeline,
        bot_tariff.fsmPipeline,
        reviews.fsmPipeline
    ])