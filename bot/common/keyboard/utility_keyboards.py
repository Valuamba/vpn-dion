from enum import IntEnum

from aiogram.filters.callback_data import CallbackData
# from  handlers.process_subscription.service import gettext as _
from common.services.vpn_client_webapi import gettext as _


class NavType(IntEnum):
    BACK = 0
    NEXT = 1
    CHECKOUT = 2
    ADD = 3
    PAY = 4
    YES = 5
    NO = 6
    CANCEL = 7
    READY = 8


class NavCD(CallbackData, prefix='nav'):
    type: NavType


class EmptyCD(CallbackData, prefix='empty'):
    pass


async def back_button(actions: [], schema: [] = None):
    if schema:
        schema.append(1)
    actions.append({'text': await _("back"), 'callback_data': NavCD(type=NavType.BACK).pack()})


async def ready_button(actions: [], schema: [] = None):
    if schema:
        schema.append(1)
    actions.append({'text': await _("ready"), 'callback_data': NavCD(type=NavType.READY).pack()})


async def get_checkout_keyboard(actions: []):
        actions.append(
            {'text': await _("arrange"), 'callback_data': NavCD(type=NavType.CHECKOUT).pack()}
        )


async def get_paument_button(actions: []):
    actions.append(
        {'text': await _("pay"), 'callback_data': NavCD(type=NavType.PAY).pack()}
    )


async def get_add_keyboard(actions: []):
    actions.append(
        { 'text': await _("add"), 'callback_data': NavCD(type=NavType.ADD).pack()}
    )