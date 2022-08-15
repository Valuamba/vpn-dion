from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.gateways import offer_gateway
from common.gateways.vpn_rest_client import VpnRestClient
from common.keyboard.utility_keyboards import NavType, NavCD
from handlers.process_subscription import Fields, DEFAULT_MONTH_INDEX, DEFAULT_DEVICE_INDEX, StateF, \
    view_device_configuration, view_payment
from handlers.process_subscription.keyboard import InlineM, SubscriptionMonthCD, SubscriptionDeviceCD
from utils.fsm.fsm_utility import edit_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from vpn_api_client.api.api import list_vpn_device_tariffs
from common.services.vpn_client_webapi import gettext as _
fsmPipeline = FSMPipeline()


async def choose_tariff_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    subscription_offers = await list_vpn_device_tariffs.asyncio(client=vpn_client)

    data = await state.get_data()

    selected_device_pkid = data.get(Fields.SelectedSubscriptionOfferPkid)

    if selected_device_pkid:
        selected_offer = next(sub for sub in subscription_offers if sub.pkid == selected_device_pkid)
    else:
        month_duration = data.get(Fields.SelectedMonthDuration)

        if not month_duration:
            month_duration = subscription_offers[0].duration_data.month_duration

        selected_offer = next(sub for sub in subscription_offers if sub.duration_data.month_duration == month_duration)

    await state.update_data(**{
        Fields.SelectedSubscriptionOfferPkid: selected_offer.pkid,
        Fields.SelectedMonthDuration: selected_offer.duration_data.month_duration,
        # Fields.SelectedSubscriptionOffer: selected_offer.__dict__
    })

    await dialog_info(ctx, bot, state, text=await _('chooseTariffMenu'),
                      reply_markup=await InlineM.get_month_keyboard(subscription_offers, selected_offer))


async def select_month_handler(ctx: CallbackQuery, callback_data: SubscriptionMonthCD, bot: Bot, state: FSMContext, vpn_client):
    await state.update_data(**{
        Fields.SelectedMonthDuration: callback_data.month_duration,
        Fields.SelectedSubscriptionOfferPkid: None
    })
    await choose_tariff_info(ctx, bot, state, vpn_client=vpn_client)


async def select_device_handler(ctx: CallbackQuery, callback_data: SubscriptionDeviceCD, bot: Bot, state: FSMContext, vpn_client):
    await state.update_data(**{Fields.SelectedSubscriptionOfferPkid: callback_data.pkid})
    await choose_tariff_info(ctx, bot, state, vpn_client)


async def checkout(ctx: CallbackQuery, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


def setup(prev_menu):
    select_device_inline = (SubscriptionDeviceCD.filter(), select_device_handler)
    select_month_inline = (SubscriptionMonthCD.filter(), select_month_handler)

    view_device_configuration.setup()
    view_payment.setup()

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectTariff, handler=checkout, information=choose_tariff_info,
                         inline_navigation_handler=[prev_menu, select_device_inline, select_month_inline],
                         filters=[NavCD.filter(F.type == NavType.CHECKOUT)],),
        view_device_configuration.fsmPipeline,
        view_payment.fsmPipeline
    ])

    # fsmPipeline.build(dp)