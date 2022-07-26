from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.gateways import offer_gateway
from common.keyboard.utility_keyboards import NavType, NavCD
from handlers.process_subscription import Fields, DEFAULT_MONTH_INDEX, DEFAULT_DEVICE_INDEX, StateF
from handlers.process_subscription.keyboard import InlineM, SubscriptionMonthCD, SubscriptionDeviceCD
from utils.fsm.fsm_utility import edit_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse

fsmPipeline = FSMPipeline()


async def choose_tariff_info(ctx: Any, bot: Bot, state: FSMContext):
    data = await state.get_data()
    selected_month = data.get(Fields.SelectedMonth, DEFAULT_MONTH_INDEX)
    selected_device = data.get(Fields.SelectedDevice, DEFAULT_DEVICE_INDEX)
    subscription_offers = await offer_gateway.get_subscription_offers()

    await dialog_info(ctx, bot, state, text="Выберите тариф:",
                      reply_markup=InlineM.get_month_keyboard(subscription_offers, selected_month, selected_device))


async def select_month_handler(ctx: CallbackQuery, callback_data: SubscriptionMonthCD, bot: Bot, state: FSMContext):
    await state.update_data(**{Fields.SelectedMonth: callback_data.month_count})
    await choose_tariff_info(ctx, bot, state)


async def select_device_handler(ctx: CallbackQuery, callback_data: SubscriptionDeviceCD, bot: Bot, state: FSMContext):
    await state.update_data(**{Fields.SelectedDevice: callback_data.devices_count})
    await choose_tariff_info(ctx, bot, state)


async def next(ctx: CallbackQuery, bot: Bot, state: FSMContext):
    await fsmPipeline.next(ctx, bot, state)


def setup():
    select_device_inline = (SubscriptionDeviceCD.filter(), select_device_handler)
    select_month_inline = (SubscriptionMonthCD.filter(), select_month_handler)

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectTariff, handler=next, information=choose_tariff_info,
                         inline_navigation_handler=[select_device_inline, select_month_inline],
                         filters=[NavCD.filter(F.type == NavType.NEXT)])
    ])

    # fsmPipeline.build(dp)