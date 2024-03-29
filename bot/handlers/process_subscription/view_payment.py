import decimal
import logging
from typing import Any

import aiogram
from aiogram import Dispatcher, Bot, F, exceptions
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, LabeledPrice, ShippingQuery, PreCheckoutQuery, WebAppData

from common.gateways import offer_gateway, instance_gateway
from common.gateways.offer_gateway import get_subscription_offers
from common.keyboard.utility_keyboards import NavType, NavCD
from common.morph import get_morph
from config import Config
from handlers.account_subscriptions.view import account_subscription_entrypoint
from handlers.process_subscription import Fields, DEFAULT_MONTH_INDEX, DEFAULT_DEVICE_INDEX, StateF, Device, \
    DeviceFields, view_tariff
from handlers.process_subscription.helpers import get_device_by_index, is_all_devices_meet_condition
from handlers.process_subscription.keyboard import InlineM, SubscriptionMonthCD, SubscriptionDeviceCD, \
    DeviceConfigureCD, DeviceConfigureMenuCD, DeviceConfigureMenuType, InstanceCountryCD, ProtocolCD, PaymentTypeCD, \
    PaymentType
from handlers.process_subscription.service import get_subscription
from utils.fsm.fsm_utility import edit_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.markup_constructor.pagination import paginate
from utils.update import get_chat_id
from vpn_api_client.api.api import retrieve_vpn_subscription, retrieve_vpn_instance
from common.services.vpn_client_webapi import gettext as _, send_post, send_get

fsmPipeline = FSMPipeline()

'''SELECT PAYMENT METHOD'''


logger = logging.getLogger(__name__)


async def select_payment_method(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    subscription_id = (await state.get_data())[Fields.SubscriptionId]
    await dialog_info(ctx, bot, state, text=await _("choosePaymentType"),
                      reply_markup=await InlineM.get_select_payment_method_markup(subscription_id))


async def select_payment_method_handler(ctx: CallbackQuery, callback_data: PaymentTypeCD, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    subscription = await get_subscription(vpn_client, data[Fields.SubscriptionId])

    alias_data = {
        'aliases': [
            'paymentTitle',
            'invoiceDescription',
            'invoiceLabel'
        ]
    }
    locales = (await send_post(vpn_client, 'bot_locale/bulk-locale', json=alias_data)).parsed
    month_duration = subscription['tariff_data']['duration_data']['month_duration']
    device_number = subscription['tariff_data']['devices_number']
    currency = 'RUB'

    labels = []
    for item in subscription['vpn_items']:
        instance = (await retrieve_vpn_instance.asyncio_detailed(pkid=str(item['instance']), client=vpn_client)).parsed
        labels.append(
            LabeledPrice(label=locales['invoiceLabel'].format(country=instance.country_data.country,
                                                              discount=f'🔻{instance.country_data.discount_percentage}%'),
                         amount=(decimal.Decimal(subscription['discounted_price']) / device_number) * 100
            )
        )

    if callback_data.type == PaymentType.YOO_MONEY:
        await bot.send_invoice(get_chat_id(ctx),
                               title=locales['paymentTitle'],
                               description=locales['invoiceDescription'].format(
                                   month_c=month_duration,
                                   month_loc=get_morph('месяц', month_duration),
                                   devices_c=device_number,
                                   devices_loc=get_morph('устройство', device_number),
                                   discount_loc=f'🔻{subscription["discount"]}%'
                               ),
                               payload=VpnPreCheckoutCD(subscription_id=subscription["pkid"]).pack(),
                               provider_token=Config.YOOMONEY_PROVIDER_TOKEN,
                               currency=currency,
                               prices=labels)


class VpnPreCheckoutCD(CallbackData, prefix="vpn-sub-precheckout"):
    subscription_id: int


async def precheckout_query_handler(pre_checkout_query: PreCheckoutQuery, bot: Bot, state: FSMContext, vpn_client):
    cd = VpnPreCheckoutCD.unpack(pre_checkout_query.invoice_payload)
    try:

        result = await send_post(vpn_client, 'subscription/create-config', json={
            "subscription_id": cd.subscription_id
        })

        if not result.status_code in [200, 201]:
            logger.error(result.parsed['details'])
            await pre_checkout_query.answer(False, error_message=result.parsed['details'])
        else:
            await pre_checkout_query.answer(True)
            await account_subscription_entrypoint(pre_checkout_query, bot, state, cd.subscription_id, vpn_client)

    except exceptions.TelegramBadRequest as e:
        if e.message == 'Bad Request: query is too old and response timeout expired or query ID is invalid':
            logger.error(e.message )
            await send_get(vpn_client, f'subscription/fail-subscription/{cd.subscription_id}/')
        raise


# async def webapp_query(ctx: Web)

async def shipping_query_handler(shipping_query: ShippingQuery):
    await shipping_query.answer(True)


def setup():
    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectPaymentMethod, handler=select_payment_method_handler,
                         information=select_payment_method,
                         filters=[PaymentTypeCD.filter()],
                         pre_checkout_query_handler=precheckout_query_handler)
    ])

