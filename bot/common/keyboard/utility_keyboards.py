from enum import IntEnum

from aiogram.dispatcher.filters.callback_data import CallbackData


class NavType(IntEnum):
    BACK = 0
    NEXT = 1
    CHECKOUT = 2
    ADD = 3
    PAY = 4


class NavCD(CallbackData, prefix='nav'):
    type: NavType


class EmptyCD(CallbackData, prefix='empty'):
    pass


def back_button(actions: [], schema: [] = None):
    if schema:
        schema.append(1)
    actions.append({'text': 'Назад', 'callback_data': NavCD(type=NavType.BACK).pack()})


def get_checkout_keyboard(actions: []):
        actions.append(
            {'text': 'Оформить', 'callback_data': NavCD(type=NavType.CHECKOUT).pack()}
        )


def get_paument_button(actions: []):
    actions.append(
        {'text': 'Оплатить', 'callback_data': NavCD(type=NavType.PAY).pack()}
    )


def get_add_keyboard(actions: []):
    actions.append(
        { 'text': 'Добавить', 'callback_data': NavCD(type=NavType.ADD).pack()}
    )