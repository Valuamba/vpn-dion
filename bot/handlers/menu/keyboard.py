from enum import IntEnum
from typing import List

from aiogram.filters.callback_data import CallbackData
from aiogram.types import WebAppInfo

from common.keyboard.utility_keyboards import back_button
from common.services.v2.types import VpnDeviceTariff
from common.services.vpn_client_webapi import get_locales
from config import Config
from utils.markup_constructor import InlineMarkupConstructor


class MenuButtonType(IntEnum):
    SUBSCRIBE = 0
    AVAILABLE_LOCATIONS = 1
    INFO_ABOUT_VPN = 2
    HELP = 3
    REFERRAL = 4
    USER_SUBSCRIPTIONS = 5
    BROADCAST = 6
    TARIFF = 7
    REVIEWS = 8


class MenuCD(CallbackData, prefix='menu'):
    type: MenuButtonType


class FastVpnTariff(CallbackData, prefix='fast-vpn-tariff'):
    tariff_id: int


class MenuMarkup(InlineMarkupConstructor):

    async def get_menu_keyboard(self, *, user_id,  tariffs: List[VpnDeviceTariff]):
        locales = await get_locales(
            'menuSubscribe',
            'mySubscribes',
            'availableLocations',
            'moreInfoAboutVPN',
            'help',
            'adviceFriends',
            'referralProgramButton',
            'broadcast'
        )

        actions = []
        schema = []

        tariffs_emojies = [ '👮', '🪬', '🛡']
        discount_emojies = [ '', '⚡', '💥']
        month_map = {
            1: 'мес',
            6: '6 мес',
            12: 'год'
        }

        for idx, t in enumerate(tariffs):
            if t.total_discount > 0:
                price_str = f'{tariffs_emojies[idx]} {t.price}р/{month_map[t.duration_data.month_duration]} ' \
                            f'{discount_emojies[idx]} дешевле на {t.total_discount}% {tariffs_emojies[idx]}'
            else:
                price_str = f'{tariffs_emojies[idx]} {t.price}р/{month_map[t.duration_data.month_duration]} {tariffs_emojies[idx]}'
            actions.append({
                'text': price_str,
                'callback_data': FastVpnTariff(tariff_id=t.pkid).pack()
            })
            schema.append(1)

        actions += [
            {'text': '🐳 Больше выгодных тарифов 🐳', 'web_app': WebAppInfo(url=Config.WEB_APP_SUBSCRIBE_LINK)},
            { 'text': locales['mySubscribes'], 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            { 'text': locales['moreInfoAboutVPN'], 'callback_data': MenuCD(type=MenuButtonType.INFO_ABOUT_VPN).pack()},
            { 'text': locales['help'], 'callback_data': MenuCD(type=MenuButtonType.HELP).pack()},
            { 'text': locales['referralProgramButton'], 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
            { 'text': 'Отзывы', 'callback_data': MenuCD(type=MenuButtonType.REVIEWS).pack()},
        ]

        schema += [1, 2, 2, 1]

        if str(user_id) in Config.ADMINISTRATORS:
            actions.append({
                'text': locales['broadcast'], 'callback_data': MenuCD(type=MenuButtonType.BROADCAST).pack()
            })
            schema.append(1)

        return self.markup(actions, schema)

    async def get_help_keyboard(self):
        actions = []
        await back_button(actions)
        return self.markup(actions, [1])

    async def get_locations_command(self):
        actions = []
        await back_button(actions)
        return self.markup(actions, [1])


InlineM = MenuMarkup()