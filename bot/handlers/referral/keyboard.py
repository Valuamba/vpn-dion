from enum import IntEnum

from aiogram.filters import callback_data
from aiogram.filters.callback_data import CallbackData

from common.keyboard.utility_keyboards import back_button, NavType, NavCD
from common.morph import get_morph
from common.services.vpn_client_webapi import get_locales
from utils.markup_constructor import InlineMarkupConstructor
from utils.markup_constructor.refactor import refactor_keyboard


class ReferralButtonType(IntEnum):
    GET_REWARD = 1
    SEE_SUBSCRIPTION = 2
    BACK_TO_MENU = 3


class ReferralCD(CallbackData, prefix='referral'):
    type: ReferralButtonType
    sub_id: int = None


class ReferralMarkup(InlineMarkupConstructor):

    async def get_referral_keyboard(self, month_subscription_count: int):
        actions = []
        locales = await get_locales(
            'getReward',
            'recommendVpn'
        )

        if month_subscription_count > 0:
            actions.append({
                'text': locales['getReward'].format(
                    month_c=month_subscription_count,
                    month_loc=get_morph('месяц', month_subscription_count)
                ),
                'callback_data': ReferralCD(type=ReferralButtonType.GET_REWARD).pack()})

        actions.append({'text': locales['recommendVpn'], 'switch_inline_query': ''})

        await back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def get_dialog_keyboard(self):
        locales = await get_locales('yes', 'no')
        actions = [
            {'text': locales['yes'], 'callback_data': NavCD(type=NavType.YES).pack()},
            {'text': locales['no'], 'callback_data': NavCD(type=NavType.BACK).pack()},
        ]
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    async def get_activated_keyboard(self, subscription_id):
        locales = await get_locales('showSubscriptionDetails', 'backToMenu')
        actions = [
            { 'text': locales['showSubscriptionDetails'], 'callback_data': ReferralCD(type=ReferralButtonType.SEE_SUBSCRIPTION, sub_id=subscription_id).pack()},
            { 'text': locales['backToMenu'], 'callback_data': NavCD(type=NavType.BACK).pack()},
        ]

        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)


InlineM = ReferralMarkup()