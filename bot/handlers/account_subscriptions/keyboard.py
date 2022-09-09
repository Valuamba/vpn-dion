from enum import IntEnum

from aiogram.filters.callback_data import CallbackData

from common.keyboard.utility_keyboards import back_button
from common.morph import get_morph
from common.services.vpn_client_webapi import gettext, get_locales
from utils.markup_constructor import InlineMarkupConstructor
from utils.markup_constructor.pagination import PaginationMetadata, PaginationInline
from utils.markup_constructor.refactor import refactor_keyboard


class SubscriptionCD(CallbackData, prefix='account_subscriptions'):
    sub_id: str


class DeviceCD(CallbackData, prefix='subscription_devices'):
    device_id: str


class ConfigFileCD(CallbackData, prefix='send_config_file'):
    device_id: str


class DeviceTutorialType(IntEnum):
    WINDOWS = 1
    IOS = 2
    LINUX = 3
    MACOS = 4
    SMART_TV = 5
    ANDROID = 6


class DeviceTutorialCD(CallbackData, prefix="device-tutorial"):
    type: DeviceTutorialType


class ListSubscriptions(InlineMarkupConstructor):
    async def get_list_subscriptions_keyboard(self, pagination: PaginationMetadata, subscriptions):
        actions = []

        subs_template = await gettext('subscription_info')

        for sub in subscriptions:
            month_duration = sub.get('month_duration', None)
            days_duration = sub.get('days_duration', None)
            device_count = sub['devices_number']
            if month_duration:
                text = subs_template.format(
                    month_c=month_duration,
                    month_loc=get_morph('месяц', month_duration),
                    devices_c=device_count,
                    devices_loc=get_morph('устройство', device_count)
                )
            elif days_duration:
                text = subs_template.format(
                    month_c=days_duration,
                    month_loc=get_morph('день', days_duration),
                    devices_c=device_count,
                    devices_loc=get_morph('устройство', device_count)
                )
            else:
                raise Exception('Wong duration of subscription.')
            actions.append({'text': text, 'callback_data': SubscriptionCD(sub_id=sub['subscription_id']).pack()})

        schema = refactor_keyboard(1, actions)
        PaginationInline().get_pagination_keyboard(actions, schema, pagination)
        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)

    async def get_list_subscription_devices_keyboard(self, pagination: PaginationMetadata, devices):
        actions = []

        for idx, device in enumerate(devices):
            actions.append({'text': f'Устройство {idx + 1} - {device["country"]}', 'callback_data': DeviceCD(device_id=device['vpn_item_id']).pack()})

        schema = refactor_keyboard(1, actions)
        PaginationInline().get_pagination_keyboard(actions, schema, pagination)
        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)

    async def get_device_details_keyboard(self, device_id, is_config_file_disabled=False):
        locales = await get_locales('getConfigFileInline', 'windowsTutorialInline', 'smartTVTutorialInline',
                                    'macOSTutorialInline', 'linuxTutorialInline', 'iosTutorialInline', 'androidTutorialInline')
        actions = []
        schema = [1, 1, 1, 1, 1, 1]
        if not is_config_file_disabled:
            actions.append(
                { 'text': locales['getConfigFileInline'], 'callback_data': ConfigFileCD(device_id=device_id).pack() },
            )
            schema.append(1)

        actions.extend([
            {'text': locales['windowsTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.WINDOWS).pack()},
            {'text': locales['linuxTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.LINUX).pack()},
            {'text': locales['macOSTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.MACOS).pack()},
            {'text': locales['smartTVTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.SMART_TV).pack()},
            {'text': locales['iosTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.IOS).pack()},
            {'text': locales['androidTutorialInline'], 'callback_data': DeviceTutorialCD(type=DeviceTutorialType.ANDROID).pack()},
        ])

        await back_button(actions)
        schema.append(1)
        return self.markup(actions, schema)


InlineM = ListSubscriptions()