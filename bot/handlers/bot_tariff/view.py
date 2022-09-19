import logging

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from common.services.v2.vpn_client_webapi import *
from common.services.vpn_client_webapi import gettext
from handlers.bot_tariff import StateF, Fields
from handlers.bot_tariff.keyboard import InlineM, CountryCD, PaymentTypeCD
from utils.fsm.fsm_utility import dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.update import get_user_id

fsmPipeline = FSMPipeline()
logger = logging.getLogger(__name__)


async def select_country_info(ctx, bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    countries = await get_available_countries(vpn_client)
    if len(countries) == 0:
        raise Exception('There are no active countries')
    if not Fields.SelectedCountryId in data:
        data[Fields.SelectedCountryId] = countries[0].pkid
        await state.update_data(data)
    country_id = data.get(Fields.SelectedCountryId)
    text = await gettext('selectCountry')
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_available_countries_keyboard(selected_country_id=country_id, countries=countries))


async def handle_selected_country(ctx: CallbackQuery, callback_data: CountryCD, bot, state: FSMContext, vpn_client):
    await state.update_data({ Fields.SelectedCountryId: callback_data.country_id })
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client)


async def handle_ready(ctx: CallbackQuery, bot, state, vpn_client):
    data = await state.get_data()
    sub_info = await create_single_device_subscription(
        user_id=get_user_id(ctx),
        country_id=data[Fields.SelectedCountryId],
        tariff_id=data[Fields.SelectedTariffId],
        vpn_client=vpn_client
    )

    await state.update_data({
        Fields.CreatedSubscription: sub_info.subscription_id, Fields.FreekassaUrl: sub_info.freekassa_url
    })
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


# PAYMENT INVOICE

async def payment_invoice_info(ctx, bot, state, vpn_client):
    data = await state.get_data()
    text = await gettext('choosePaymentType')
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_invoice_keyboard(
                          subscription_id=data[Fields.CreatedSubscription],
                          freekassa_url=data[Fields.FreekassaUrl]
                      ))


async def handle_payment_method(ctx: CallbackQuery, bot, state, vpn_client):
    pass


def setup(prev_menu):
    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectCountry, handler=handle_selected_country,
                         filters=[CountryCD.filter()],
                         information=select_country_info,
                         inline_navigation_handler=[
                             (NavCD.filter(F.type==NavType.READY), handle_ready),
                             prev_menu
                         ]
        ),
        CallbackResponse(state=StateF.SelectPaymentMethod, handler=handle_payment_method,
                         filters=[PaymentTypeCD.filter()],
                         information=payment_invoice_info,
                         inline_navigation_handler=[
                             # prev_menu
                         ]
                         ),
    ])