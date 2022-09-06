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


class MenuCD(CallbackData, prefix='menu'):
    type: MenuButtonType


class MenuMarkup(InlineMarkupConstructor):

    async def get_menu_keyboard(self):
        locales = await get_locales(
            'menuSubscribe',
            'mySubscribes',
            'availableLocations',
            'moreInfoAboutVPN',
            'help',
            'adviceFriends',
            'referralProgramButton'
        )

        actions = [
            { 'text': locales['menuSubscribe'], 'web_app': WebAppInfo(url=Config.WEB_APP_SUBSCRIBE_LINK)},
            { 'text': locales['mySubscribes'], 'callback_data': MenuCD(type=MenuButtonType.USER_SUBSCRIPTIONS).pack()},
            { 'text': locales['availableLocations'], 'callback_data': MenuCD(type=MenuButtonType.AVAILABLE_LOCATIONS).pack()},
            { 'text': locales['moreInfoAboutVPN'], 'callback_data': MenuCD(type=MenuButtonType.INFO_ABOUT_VPN).pack()},
            { 'text': locales['help'], 'callback_data': MenuCD(type=MenuButtonType.HELP).pack()},
            { 'text': locales['referralProgramButton'], 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
            # { 'text': locales['adviceFriends'], 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
        ]

        schema = [1, 1, 1, 2, 1]
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