from enum import IntEnum

from aiogram.dispatcher.filters.callback_data import CallbackData


class NavType(IntEnum):
    BACK = 0
    NEXT = 1


class NavCD(CallbackData, prefix='nav'):
    type: NavType


class EmptyCD(CallbackData, prefix='empty'):
    pass


def back_button(actions: [], schema: [] = None):
    if schema:
        schema.append(1)
    actions.append({'text': 'Назад', 'callback_data': NavCD(type=NavType.BACK).pack()})