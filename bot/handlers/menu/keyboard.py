from enum import IntEnum

from aiogram.dispatcher.filters.callback_data import CallbackData

from utils.markup_constructor import InlineMarkupConstructor


class MenuButtonType(IntEnum):
    SUBSCRIBE = 0
    AVAILABLE_LOCATIONS = 1
    INFO_ABOUT_VPN = 2
    HELP = 3
    REFERRAL = 4


class MenuCD(CallbackData, prefix='menu'):
    type: MenuButtonType


class MenuMarkup(InlineMarkupConstructor):

    def get_menu_keyboard(self):
        actions = [
            { 'text': 'Подписаться', 'callback_data': MenuCD(type=MenuButtonType.SUBSCRIBE).pack()},
            { 'text': 'Доступные локации', 'callback_data': MenuCD(type=MenuButtonType.AVAILABLE_LOCATIONS).pack()},
            { 'text': 'Узнать о VPN', 'callback_data': MenuCD(type=MenuButtonType.INFO_ABOUT_VPN).pack()},
            { 'text': 'Помощь', 'callback_data': MenuCD(type=MenuButtonType.HELP).pack()},
            { 'text': 'Посоветовать друзьям', 'callback_data': MenuCD(type=MenuButtonType.REFERRAL).pack()},
        ]

        schema = [1, 1, 2, 1]
        return self.markup(actions, schema)


InlineM = MenuMarkup()