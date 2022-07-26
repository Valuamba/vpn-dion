from enum import IntEnum

from aiogram.dispatcher.filters.callback_data import CallbackData

from utils.markup_constructor import InlineMarkupConstructor


class MenuType(IntEnum):
    ChooseTariff = 0
    AvailableLocations = 1
    VpnDetails = 2
    Help = 3
    ShareWithFriends = 4
    Partnership = 5


class MenuCD(CallbackData, prefix="menu-cd"):
    type: MenuType


class StartCommandIM(InlineMarkupConstructor):

    def get_start_keyboard(self):
        actions = [
            { 'text': 'Выбрать тариф', 'callback_data': MenuCD(type=MenuType.ChooseTariff).pack() },
            { 'text': 'Доступные локации', 'callback_data': MenuCD(type=MenuType.AvailableLocations).pack() },
            { 'text': 'Узнать о VPN', 'callback_data': MenuCD(type=MenuType.VpnDetails).pack() },
            { 'text': 'Помощь', 'callback_data': MenuCD(type=MenuType.Help).pack() },
            { 'text': 'Посоветовать друзьям', 'callback_data': MenuCD(type=MenuType.ShareWithFriends).pack() },
            { 'text': 'Партнерство', 'callback_data': MenuCD(type=MenuType.Partnership).pack() },
        ]

        schema = [1, 1, 2, 1, 1]
        return self.markup(actions, schema)


