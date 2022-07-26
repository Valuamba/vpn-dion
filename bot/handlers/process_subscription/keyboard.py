from functools import reduce
from typing import List, Dict

from aiogram.dispatcher.filters.callback_data import CallbackData

from common.gateways import offer_gateway
from common.keyboard.utility_keyboards import back_button, EmptyCD
from common.models.subscription_offer import SubscriptionOffer
from handlers.process_subscription.helpers import get_month_text, get_device_locale
from utils.markup_constructor import InlineMarkupConstructor
import pandas
from functools import reduce
from collections import defaultdict

from utils.markup_constructor.refactor import refactor_keyboard


class SubscriptionMonthCD(CallbackData, prefix='month'):
    index: int


class SubscriptionDeviceCD(CallbackData, prefix='subs-device'):
    index: int


class PaymentCalculatorMarkup(InlineMarkupConstructor):

    SELECT_SYMBOL = '✅'
    EXPAND_TRUE_SYMBOL = '↘️'
    EXPAND_FALSE_SYMBOL = '➖'
    month_text = "%s месяц"

    def get_month_keyboard(self, subscription_offers: List[SubscriptionOffer], selected_month_index: int, selected_device_idx: int):
        # subscription_offers = offer_gateway.get_subscription_offers()
        offers = self.__group_by_month(subscription_offers)

        actions = []
        for index, (month, month_offers) in enumerate(offers.items()):
            text = get_month_text(month)
            if selected_month_index == index:
                text += f' {self.EXPAND_TRUE_SYMBOL}'
                actions.append({'text': text, 'callback_data': EmptyCD().pack()})
                actions += self.device_offer_keyboard(month_offers, selected_device_idx)
            else:
                text += f' {self.EXPAND_FALSE_SYMBOL}'
                actions.append({'text': text, 'callback_data': SubscriptionMonthCD(index=index).pack()})

        back_button(actions)
        schema = refactor_keyboard(1, actions)
        return self.markup(actions, schema)

    def device_offer_keyboard(self, subscription_offers: List[SubscriptionOffer], selected_device_idx: int):
        actions = []

        for idx, sub in enumerate(subscription_offers):
            text = get_device_locale(sub.devices_count, 1000, sub.discount_percentage, 'RUB')
            callback_data = SubscriptionDeviceCD(devices_count=sub.devices_count).pack()
            if idx == selected_device_idx:
                text += ' ' + self.SELECT_SYMBOL
                callback_data = EmptyCD().pack()

            actions.append({
                'text': text,
                'callback_data': callback_data
            })

        return actions

    def __group_by_month(self, subscription_offers: List[SubscriptionOffer]) -> Dict[int, List[SubscriptionOffer]]:
        dict = {}

        for subscription in subscription_offers:
            if subscription.month_duration in dict.keys():
                subs: List[SubscriptionOffer] = dict[subscription.month_duration]
                subs.append(subscription)
                dict[subscription.month_duration] = subs
            else:
                dict[subscription.month_duration] = [subscription]

        return dict


InlineM = PaymentCalculatorMarkup()

# PaymentCalculatorMarkup().get_month_keyboard(None)