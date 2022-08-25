from aiogram.filters.callback_data import CallbackData

from common.keyboard.utility_keyboards import back_button
from common.morph import get_morph
from common.services.vpn_client_webapi import gettext
from utils.markup_constructor import InlineMarkupConstructor
from utils.markup_constructor.pagination import PaginationMetadata, PaginationInline
from utils.markup_constructor.refactor import refactor_keyboard


class SubscriptionCD(CallbackData, prefix='account_subscriptions'):
    sub_id: str


class DeviceCD(CallbackData, prefix='subscription_devices'):
    device_id: str


class ListSubscriptions(InlineMarkupConstructor):
    async def get_list_subscriptions_keyboard(self, pagination: PaginationMetadata, subscriptions):
        actions = []

        subs_template = await gettext('subscription_info')

        for sub in subscriptions:
            month_duration = sub['month_duration']
            device_count = sub['devices_number']
            text = subs_template.format(
                month_c=month_duration,
                month_loc=get_morph('месяц', month_duration),
                devices_c=device_count,
                devices_loc=get_morph('устройство', device_count)
            )
            actions.append({'text': text, 'callback_data': SubscriptionCD(sub_id=sub['subscription_id']).pack()})

        schema = refactor_keyboard(1, actions)
        PaginationInline().get_pagination_keyboard(actions, schema, pagination)
        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)

    async def get_list_subscription_devices_keyboard(self, pagination: PaginationMetadata, devices):
        actions = []

        for idx, device in enumerate(devices):
            actions.append({'text': f'Устройство {idx + 1} - {device["instance_data"]["country_data"]["country"]}', 'callback_data': DeviceCD(device_id=device['pkid']).pack()})

        schema = refactor_keyboard(1, actions)
        PaginationInline().get_pagination_keyboard(actions, schema, pagination)
        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)

    async def get_device_details_keyboard(self):
        actions = []
        await back_button(actions)
        return self.markup(actions, [1])


InlineM = ListSubscriptions()