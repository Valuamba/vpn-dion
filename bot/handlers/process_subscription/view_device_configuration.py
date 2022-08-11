from typing import Any

from aiogram import Dispatcher, Bot, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.gateways import offer_gateway, instance_gateway
from common.gateways.offer_gateway import get_subscription_offers
from common.keyboard.utility_keyboards import NavType, NavCD
from handlers.process_subscription import Fields, DEFAULT_MONTH_INDEX, DEFAULT_DEVICE_INDEX, StateF, Device, \
    DeviceFields, view_tariff
from handlers.process_subscription.helpers import get_device_by_index, is_all_devices_meet_condition
from handlers.process_subscription.keyboard import InlineM, SubscriptionMonthCD, SubscriptionDeviceCD, \
    DeviceConfigureCD, DeviceConfigureMenuCD, DeviceConfigureMenuType, InstanceCountryCD, ProtocolCD
from handlers.process_subscription.service import get_devices_form_data, create_subscription
from utils.fsm.fsm_utility import edit_main_message, dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.markup_constructor.pagination import paginate
from utils.update import get_user_id
from vpn_api_client.api.api import retrieve_vpn_device_tariff, list_vpn_countrys, list_vpn_protocols
from  handlers.process_subscription.service import gettext as _

fsmPipeline = FSMPipeline()

'''DEVICE MENU'''


async def add_device_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    subscription_offer = await retrieve_vpn_device_tariff.asyncio(data[Fields.SelectedSubscriptionOfferPkid], client=vpn_client)
    form = await get_devices_form_data(data, subscription_offer, vpn_client)
    devices = data.get(Fields.Devices, None)
    is_payment_button_visible = is_all_devices_meet_condition(devices, subscription_offer.devices_number)
    await dialog_info(ctx, bot, state, text=form,
                      reply_markup=await InlineM.get_devices_manager_keyboard(
                          subscription_offer.devices_number, subscription_offer.operation,
                          is_payment_button_visible=is_payment_button_visible
                      ))


async def handle_select_device_to_configure(ctx: CallbackQuery, callback_data: DeviceConfigureCD, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    data[Fields.ConfiguredDeviceIndex] = callback_data.device_index
    devices = data.setdefault(Fields.Devices, [])

    if not any(get_device_by_index(devices, callback_data.device_index)):
        devices.append({
            DeviceFields.DeviceIndex: callback_data.device_index,
            DeviceFields.SelectedProtocolPk: None,
            DeviceFields.SelectedCountryPk: None
        })

    await state.update_data(data)
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


async def get_payment_checkout_handler(ctx, bot, state, vpn_client):
    data = await state.get_data()
    subscribe_id = await create_subscription(data, get_user_id(ctx), vpn_client)
    data[Fields.SubscriptionId] = subscribe_id
    await state.update_data(data)
    await view_tariff.fsmPipeline.move_to(ctx, bot, state, StateF.SelectPaymentMethod, vpn_client=vpn_client)


'''MENU'''


async def device_menu_configuration(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    tariff = await retrieve_vpn_device_tariff.asyncio(data[Fields.SelectedSubscriptionOfferPkid], client=vpn_client)
    form = await get_devices_form_data(await state.get_data(), tariff, vpn_client)
    await dialog_info(ctx, bot, state, text=form,
                      reply_markup=await InlineM.get_device_configuration_menu())


async def device_menu_configuration_handler(ctx: CallbackQuery, callback_data: DeviceConfigureMenuCD, bot: Bot, state: FSMContext, vpn_client):
    if callback_data.type == DeviceConfigureMenuType.SELECT_COUNTRY:
        await fsmPipeline.move_to(ctx, bot, state, StateF.ChooseLocation, vpn_client=vpn_client)
    elif callback_data.type == DeviceConfigureMenuType.SELECT_PROTOCOL:
        await fsmPipeline.move_to(ctx, bot, state, StateF.ChooseProtocol, vpn_client=vpn_client)


'''SELECT COUNTRY'''


async def select_country_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    countries = await list_vpn_countrys.asyncio(client=vpn_client)
    metadata = paginate(len(countries), 1, 5)
    countries = countries[metadata.start:metadata.end]
    await dialog_info(ctx, bot, state, text=await _("chooseCountry"),
                      reply_markup=await InlineM.get_country_keyboard(metadata, countries))


async def select_country_handler(ctx: CallbackQuery, callback_data: InstanceCountryCD,  bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    device = next(get_device_by_index(data[Fields.Devices], data[Fields.ConfiguredDeviceIndex]))
    device[DeviceFields.SelectedCountryPk] = callback_data.pkid
    await state.update_data(data)
    await fsmPipeline.move_to(ctx, bot, state, StateF.ConfigureDevice, vpn_client=vpn_client)


'''SELECT PROTOCOL'''


async def select_protocol_info(ctx: Any, bot: Bot, state: FSMContext, vpn_client):
    protocols = await list_vpn_protocols.asyncio(client=vpn_client)
    await dialog_info(ctx, bot, state, text=await _("chooseProtocol"),
                      reply_markup=await InlineM.get_protocol_keyboard(protocols))


async def select_protocol_handler(ctx: CallbackQuery, callback_data: ProtocolCD, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    device = next(get_device_by_index(data[Fields.Devices], data[Fields.ConfiguredDeviceIndex]))
    device[DeviceFields.SelectedProtocolPk] = callback_data.pkid
    await state.update_data(data)
    await fsmPipeline.move_to(ctx, bot, state, StateF.ConfigureDevice, vpn_client=vpn_client)


'''INLINE'''


async def back_to_device_menu(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.move_to(ctx, bot, state, StateF.ConfigureDevice, vpn_client=vpn_client)


async def prev(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.prev(ctx, bot, state, vpn_client=vpn_client)


async def back_to_tariff(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state:FSMContext, vpn_client):
    await state.update_data(**{Fields.Devices: []})
    await view_tariff.fsmPipeline.move_to(ctx, bot, state, StateF.SelectTariff, vpn_client=vpn_client)


'''SETUP'''


def setup():
    prev_inline = (NavCD.filter(F.type==NavType.BACK), prev)
    back_to_device_menu_inline = (NavCD.filter(F.type==NavType.BACK), back_to_device_menu)

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SelectDevice, handler=handle_select_device_to_configure,
                         information=add_device_info,
                         filters=[DeviceConfigureCD.filter()],
                         inline_navigation_handler=[
                             (NavCD.filter(F.type==NavType.BACK), back_to_tariff),
                             (NavCD.filter(F.type==NavType.PAY), get_payment_checkout_handler)
                         ]),
        CallbackResponse(state=StateF.ConfigureDevice, handler=device_menu_configuration_handler,
                         information=device_menu_configuration,
                         filters=[DeviceConfigureMenuCD.filter()],
                         inline_navigation_handler=[prev_inline]
                         ),
        CallbackResponse(state=StateF.ChooseLocation, handler=select_country_handler,
                         information=select_country_info,
                         filters=[InstanceCountryCD.filter()],
                         inline_navigation_handler=[back_to_device_menu_inline]),
        CallbackResponse(state=StateF.ChooseProtocol, handler=select_protocol_handler,
                         information=select_protocol_info,
                         filters=[ProtocolCD.filter()],
                         inline_navigation_handler=[back_to_device_menu_inline])
    ])

