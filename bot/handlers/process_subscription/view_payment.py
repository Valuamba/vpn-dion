import decimal
from typing import Any

import aiogram
from aiogram import Dispatcher, Bot, F, exceptions
from aiogram.dispatcher.filters.callback_data import CallbackData
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery, LabeledPrice, ShippingQuery, PreCheckoutQuery
from vpn_api_client.models import VpnSubscription, UpdateVpnSubscription, UpdateVpnSubscriptionStatus, \
    VpnSubscriptionStatus

from common.gateways import offer_gateway, instance_gateway
from common.gateways.offer_gateway import get_subscription_offers
from common.keyboard.utility_keyboards import NavType, NavCD
from handlers.process_subscription import Fields, DEFAULT_MONTH_INDEX, DEFAULT_DEVICE_INDEX, StateF, Device, \
    DeviceFields, view_tariff
from handlers.process_subscription.helpers import get_device_by_index, is_all_devices_meet_condition
from handlers.process_subscription.keyboard import InlineM, SubscriptionMonthCD, SubscriptionDeviceCD, \
    DeviceConfigureCD, DeviceConfigureMenuCD, DeviceConfigureMenuType, InstanceCountryCD, ProtocolCD, PaymentTypeCD, \
    PaymentType
from utils.fsm.fsm_utility import edit_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.markup_constructor.pagination import paginate
from utils.update import get_chat_id
from vpn_api_client.api.api import retrieve_vpn_subscription, update_vpn_subscription
from  handlers.process_subscription.service import gettext as _

fsmPipeline = FSMPipeline()

'''SELECT PAYMENT METHOD'''


async def select_payment_method(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    subscription_id = (await state.get_data())[Fields.SubscriptionId]
    await dialog_info(ctx, bot, state, text=await _("choosePaymentType"),
                      reply_markup=await InlineM.get_select_payment_method_markup(subscription_id))


async def select_payment_method_handler(ctx: CallbackQuery, callback_data: PaymentTypeCD, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    subscription = await retrieve_vpn_subscription.asyncio(data[Fields.SubscriptionId], client=vpn_client)

    if callback_data.type == PaymentType.YOO_MONEY:
        await bot.send_invoice(get_chat_id(ctx),
                               title='VPN - 12 месяцев, 2 устройства',
                               description='Подписка на VPN',
                               payload=VpnPreCheckoutCD(subscription_id=subscription.pkid).pack(),
                               provider_token='381764678:TEST:40401',
                               currency='RUB',
                               prices=[
                                   LabeledPrice(label='Устройство 1', amount=decimal.Decimal(subscription.total_price) * 100),
                                   # LabeledPrice(label='Устройство 2', amount=decimal.Decimal(subscription.total_price) * 100),
                                   # LabeledPrice(label='Устройство 3', amount=decimal.Decimal(subscription.total_price) * 100),
                               ])


class VpnPreCheckoutCD(CallbackData, prefix="vpn-sub-precheckout"):
    subscription_id: int


async def precheckout_query_handler(pre_checkout_query: PreCheckoutQuery, vpn_client):
    cd = VpnPreCheckoutCD.unpack(pre_checkout_query.invoice_payload)
    try:
        subscription = await retrieve_vpn_subscription.asyncio(str(cd.subscription_id), client=vpn_client)

        #waiting for payment
        if subscription.status != VpnSubscriptionStatus.WAITING_FOR_PAYMENT:
            await pre_checkout_query.answer(False, error_message=await _("paymentCannotBeProcessed"))

        else:
            updated_subscription = UpdateVpnSubscription(status=UpdateVpnSubscriptionStatus.PAID)
            await update_vpn_subscription.asyncio(pkid=str(cd.subscription_id), client=vpn_client, form_data=updated_subscription, json_body=updated_subscription, multipart_data=updated_subscription)
            await pre_checkout_query.answer(True)

    except exceptions.TelegramBadRequest as e:
        if e.message == 'Bad Request: query is too old and response timeout expired or query ID is invalid':
            updated_subscription = UpdateVpnSubscription(status=UpdateVpnSubscriptionStatus.PAYMENT_WAS_FAILED)
            await update_vpn_subscription.asyncio(pkid=str(cd.subscription_id), client=vpn_client,
                                                  form_data=updated_subscription, json_body=updated_subscription,
                                                  multipart_data=updated_subscription
                                                  )
        raise


async def shipping_query_handler(shipping_query: ShippingQuery):
    await shipping_query.answer(True)


def setup():
    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectPaymentMethod, handler=select_payment_method_handler,
                         information=select_payment_method,
                         filters=[PaymentTypeCD.filter()],
                         pre_checkout_query_handler=precheckout_query_handler)
    ])

