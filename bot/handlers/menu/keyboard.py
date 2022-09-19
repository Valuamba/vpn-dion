from enum import IntEnum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import WebAppInfo

from common.keyboard.utility_keyboards import back_button
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


class MenuCD(CallbackData, prefix='menu'):
    type: MenuButtonType


class FastVpnTariff(CallbackData, prefix='fast-vpn-tariff'):
    tariff_id: int


class MenuMarkup(InlineMarkupConstructor):

    async def get_menu_keyboard(self, user_id):
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

        actions = [
            # { 'text': '🐳 Выбрать тариф', 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            { 'text': '👮 290р/мес 👮', 'callback_data': FastVpnTariff(tariff_id=1).pack() },
            # { 'text': '🪬 790р/6 мес 🪬 скидка 20% 🎉', 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            { 'text': '🪬 790р/6 мес ⚡ дешевле на 20% 🪬', 'callback_data': FastVpnTariff(tariff_id=2).pack() },
            { 'text': '🛡 1800р/год 💥 дешевле на 40% 🛡', 'callback_data': FastVpnTariff(tariff_id=3).pack() },
            {'text': '🐳 Больше выгодных тарифов 🐳', 'web_app': WebAppInfo(url=Config.WEB_APP_SUBSCRIBE_LINK)},
            # { 'text': '12 месяцев 790₽ (дешевле на 35%)', 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            { 'text': locales['mySubscribes'], 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            # { 'text': locales['availableLocations'], 'callback_data': MenuCD(type=MenuButtonType.AVAILABLE_LOCATIONS).pack()},
            { 'text': locales['moreInfoAboutVPN'], 'callback_data': MenuCD(type=MenuButtonType.INFO_ABOUT_VPN).pack()},
            { 'text': locales['help'], 'callback_data': MenuCD(type=MenuButtonType.HELP).pack()},
            { 'text': locales['referralProgramButton'], 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
            # { 'text': locales['adviceFriends'], 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
        ]

        schema = [1, 1, 1, 1, 2, 2]

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