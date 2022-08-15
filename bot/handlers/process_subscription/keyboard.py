from enum import IntEnum
from functools import reduce
from typing import List, Dict
from urllib.parse import urljoin

from aiogram.dispatcher.filters.callback_data import CallbackData
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from vpn_api_client.models import VpnDeviceTariff, VpnCountry, VpnProtocol

from common.gateways import offer_gateway
from common.keyboard.utility_keyboards import back_button, EmptyCD, get_checkout_keyboard, get_add_keyboard, \
    get_paument_button
from common.models.instnace import Instance
from common.models.protocol import Protocol
from common.models.subscription_offer import SubscriptionOffer, SubscriptionDurationOffer, SubscriptionDeviceOffer, \
    SubscriptionOfferDevicesType
from common.morph import get_morph
from config import Config
from handlers.process_subscription import Fields, DeviceFields
from handlers.process_subscription.helpers import group_subscription_offers_by_month, is_device_configured, \
    is_all_devices_meet_condition
from utils.markup_constructor import InlineMarkupConstructor
import pandas
from functools import reduce
from collections import defaultdict

from utils.markup_constructor.pagination import PaginationMetadata, PaginationInline
from utils.markup_constructor.refactor import refactor_keyboard
from common.services.vpn_client_webapi import gettext as _, get_locales, gettext


class DeviceConfigureMenuType(IntEnum):
    SELECT_COUNTRY = 0
    SELECT_PROTOCOL = 1


class PaymentType(IntEnum):
    RUSSIAN_CARD = 1
    FOREIGN_CARD = 2
    YOO_MONEY = 3
    CRYPTO_CURRENCY = 4
    QIWI = 5
    TINKOFF = 6


class SubscriptionMonthCD(CallbackData, prefix='month'):
    month_duration: int


class SubscriptionDeviceCD(CallbackData, prefix='subs-device'):
    pkid: int


class DeviceConfigureCD(CallbackData, prefix="device-configure"):
    device_index: int


class DeviceConfigureMenuCD(CallbackData, prefix="device-configure-menu"):
    type: DeviceConfigureMenuType


class InstanceCountryCD(CallbackData, prefix="instance-country"):
    pkid: int


class ProtocolCD(CallbackData, prefix="protocol"):
    pkid: int


class PaymentTypeCD(CallbackData, prefix="payment-method"):
    type: PaymentType
    subscription_id: int


class PaymentCalculatorMarkup(InlineMarkupConstructor):

    SELECT_SYMBOL = '✅'
    EXPAND_TRUE_SYMBOL = '↘️'
    EXPAND_FALSE_SYMBOL = '➖'
    month_text = "%s месяц"

    async def get_month_keyboard(self, subscription_offers: List[VpnDeviceTariff], selected_offer: VpnDeviceTariff):
        grouped_subs = group_subscription_offers_by_month(subscription_offers)

        actions = []
        for month, devices in grouped_subs.items():
            text = (await _("monthDropDownHeader")).format(month=month,
                                                           month_locale=get_morph('месяц', month))
            if month == selected_offer.duration_data.month_duration:
                text += f' {self.EXPAND_TRUE_SYMBOL}'
                actions.append({'text': text, 'callback_data': EmptyCD().pack()})
                actions += await self.device_offer_keyboard(devices, selected_offer.pkid)
            else:
                text += f' {self.EXPAND_FALSE_SYMBOL}'
                actions.append({'text': text, 'callback_data':  SubscriptionMonthCD(month_duration=month).pack()})

        await get_checkout_keyboard(actions)
        await back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def device_offer_keyboard(self, device_offers: List[VpnDeviceTariff], device_pkid: int = None):
        actions = []
        device_tariff_template = await _("deviceTariff")

        for device_offer in device_offers:
            text = device_tariff_template.format(device_c=device_offer.devices_number,
                                                 device_loc=get_morph('устройство', device_offer.devices_number),
                                                 price=device_offer.discounted_price,
                                                 curr=device_offer.duration_data.currency,
                                                 discount=device_offer.discount_percentage)
            callback_data = SubscriptionDeviceCD(pkid=device_offer.pkid).pack()
            if device_pkid == device_offer.pkid:
                text += ' ' + self.SELECT_SYMBOL
                callback_data = EmptyCD().pack()

            actions.append({
                'text': text,
                'callback_data': callback_data
            })

        return actions

    async def get_devices_manager_keyboard(self, devices, devices_number, device_operation):
        actions = []
        is_payment_button_visible = is_all_devices_meet_condition(devices, devices_number)

        locales = await get_locales("addDevice", 'changeDeviceButton')

        for index in range(devices_number):
            if devices and index <= len(devices) - 1 and is_device_configured(devices[index]):
                actions.append({'text': locales['changeDeviceButton'].format(idx=index + 1),
                                'callback_data': DeviceConfigureCD(device_index=index).pack()}
                               )
            else:
                actions.append({'text': locales['addDevice'].format(index=index + 1),
                                'callback_data': DeviceConfigureCD(device_index=index).pack()})

        if device_operation == "greater_than_or_equal":
            await get_add_keyboard(actions)

        if is_payment_button_visible:
            await get_paument_button(actions)

        await back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def get_device_configuration_menu(self, device):

        locales = await get_locales("chooseCountry", "chooseProtocol", "changeCountry", "changeProtocol")

        actions = []

        if device and device.get(DeviceFields.SelectedCountryPk, None):
            actions.append({ 'text': locales['changeCountry'], 'callback_data': DeviceConfigureMenuCD(type=DeviceConfigureMenuType.SELECT_COUNTRY).pack()})
        else:
            actions.append({ 'text': locales['chooseCountry'], 'callback_data': DeviceConfigureMenuCD(type=DeviceConfigureMenuType.SELECT_COUNTRY).pack()})

        if device and device.get(DeviceFields.SelectedProtocolPk, None):
            actions.append({ 'text': locales['changeProtocol'], 'callback_data': DeviceConfigureMenuCD(type=DeviceConfigureMenuType.SELECT_PROTOCOL).pack()})
        else:
            actions.append({'text': locales['chooseProtocol'], 'callback_data': DeviceConfigureMenuCD(type=DeviceConfigureMenuType.SELECT_PROTOCOL).pack()})

        await back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def get_country_keyboard(self, pagination: PaginationMetadata, countries: List[VpnCountry]):
        actions = []

        for country in countries:
            actions.append({ 'text': country.country, 'callback_data': InstanceCountryCD(pkid=country.pkid).pack()})

        schema = refactor_keyboard(1, actions)
        PaginationInline().get_pagination_keyboard(actions, schema, pagination)
        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)

    async def get_protocol_keyboard(self, protocols: List[VpnProtocol]):
        actions = []

        for protocol in protocols:
            actions.append({'text': protocol.protocol, 'callback_data': ProtocolCD(pkid=protocol.pkid).pack()})

        await back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def get_select_payment_method_markup(self, subscription_id: int):
        freekassa_url = urljoin(Config.VPN_REST_HTTPS, f'payment_processing/checkout/?subscription_id={subscription_id}&payment_provider=freekassa')
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="YooMoney", callback_data=PaymentTypeCD(type=PaymentType.YOO_MONEY, subscription_id=subscription_id).pack())],
            [InlineKeyboardButton(text="Bitcoin, ETH, Qiwi", web_app=WebAppInfo(url=freekassa_url))]
        ])
        # actions = [
        #     {'text': 'Bitcoin, ETH, Qiwi', 'web_app': WebAppInfo(url=freekassa_url)},
        #     {'text': 'YooMoney', 'callback_data': PaymentTypeCD(type=PaymentType.YOO_MONEY, subscription_id=subscription_id).pack()},
        #     # { 'text': 'Банковской картой (Россия)', 'callback_data': PaymentTypeCD(type=PaymentType.RUSSIAN_CARD, subscription_id=subscription_id).pack() },
        #     # { 'text': 'Банковской картой (вне России)', 'callback_data': PaymentTypeCD(type=PaymentType.FOREIGN_CARD, subscription_id=subscription_id).pack() },
        #     # { 'text': 'Qiwi', 'callback_data': PaymentTypeCD(type=PaymentType.QIWI, subscription_id=subscription_id).pack() },
        #     # { 'text': 'Tinkoff', 'callback_data': PaymentTypeCD(type=PaymentType.TINKOFF, subscription_id=subscription_id).pack() },
        # ]
        # await back_button(actions)
        # schema = refactor_keyboard(1, actions)
        # return self.markup(actions, schema)

    def __group_by_month(self, subscription_offers: List[SubscriptionOffer]) -> Dict[int, List[SubscriptionOffer]]:
        dict = {}

        for subscription in subscription_offers:
            if subscription.month_duration in dict.keys():
                subs: List[SubscriptionOffer] = dict[subscription.month_duration]
                subs.append(subscription)
                dict[subscription.month_duration] = subs
            else:
                dict[subscription.month_duration] = [subscription]

        return dict


InlineM = PaymentCalculatorMarkup()

# PaymentCalculatorMarkup().get_month_keyboard(None)