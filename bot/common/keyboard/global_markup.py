from aiogram.filters.callback_data import CallbackData

from common.services.vpn_client_webapi import gettext
from utils.markup_constructor import InlineMarkupConstructor


class GlobalSubscriptionCD(CallbackData, prefix='vpn-subscription'):
    subscription_id: int


class GlobalKeyboardMarkup(InlineMarkupConstructor):

    async def get_nav_to_sub_details(self, subscription_id):
        text = await gettext('seeSubDetails')
        actions = [
            { 'text': text, 'callback_data': GlobalSubscriptionCD(subscription_id=subscription_id).pack()}
        ]
        return self.markup(actions, [1])