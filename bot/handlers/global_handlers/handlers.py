from aiogram import Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.global_markup import GlobalSubscriptionCD
from handlers.account_subscriptions.view import redirect_to_sub_devices_info


async def handle_see_subscription(ctx: CallbackQuery, callback_data: GlobalSubscriptionCD, bot: Bot, state: FSMContext, vpn_client):
    await redirect_to_sub_devices_info(ctx, bot, state, vpn_client, callback_data.subscription_id)


def setup(dp: Dispatcher):

    dp.callback_query.register(handle_see_subscription, GlobalSubscriptionCD.filter())