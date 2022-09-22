from enum import IntEnum
from typing import List

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup

from common.keyboard.utility_keyboards import back_button, ready_button
from common.services.v2.types import VpnCountry
from common.services.vpn_client_webapi import get_locales
from utils.markup_constructor import InlineMarkupConstructor
from utils.markup_constructor.refactor import refactor_keyboard

FREE_SELECTOR = '○'
FILLED_SELECTOR = '●'



class PaymentType(IntEnum):
    RUSSIAN_CARD = 1
    FOREIGN_CARD = 2
    YOO_MONEY = 3
    CRYPTO_CURRENCY = 4
    QIWI = 5
    TINKOFF = 6


class PaymentTypeCD(CallbackData, prefix="payment-method"):
    type: PaymentType
    subscription_id: int


class CountryCD(CallbackData, prefix='vpn-country'):
    country_id: int


class BotTariffMarkup(InlineMarkupConstructor):

    async def get_available_countries_keyboard(self, *, selected_country_id: int, countries: List[VpnCountry]):
        actions = []
        for c in countries:
            text = FILLED_SELECTOR + ' ' + c.locale_ru if c.pkid == selected_country_id else FREE_SELECTOR + ' ' +c.locale_ru
            actions.append({
                'text': text, 'callback_data': CountryCD(country_id=c.pkid).pack()
            })
        schema = refactor_keyboard(2, actions)
        await back_button(actions)
        await ready_button(actions)
        schema.append(2)
        return self.markup(actions, schema)

    async def get_invoice_keyboard(self, *, subscription_id: int, freekassa_url: str):
        locales = await get_locales('yoomoneyProvider', 'freekassaProvider')
        actions = [
            # { 'text': locales['yoomoneyProvider'], 'callback_data': PaymentTypeCD(type=PaymentType.YOO_MONEY, subscription_id=subscription_id).pack() },
            { 'text': locales['freekassaProvider'], 'url': freekassa_url}
        ]
        schema = [1]
        return self.markup(actions, schema)




InlineM = BotTariffMarkup()