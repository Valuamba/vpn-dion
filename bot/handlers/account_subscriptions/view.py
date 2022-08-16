from aiogram import Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from handlers.account_subscriptions import StateF, Fields
from handlers.account_subscriptions.keyboard import InlineM, SubscriptionCD, DeviceCD
from handlers.account_subscriptions.serivce import get_all_user_subscriptions, get_all_subscription_devices, \
    get_device_vpn_settings, get_device_qrcode
from  handlers.process_subscription.service import gettext as _
from utils.fsm.fsm_utility import dialog_info, MessageType
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.markup_constructor.pagination import paginate, PaginationCD
from utils.update import get_user_id

fsmPipeline = FSMPipeline()


# SUBSCRIPTIONS LIST
async def subscriptions_list(ctx, bot: Bot, state: FSMContext, vpn_client, page = 1):
    subscriptions = await get_all_user_subscriptions(get_user_id(ctx), vpn_client)
    metadata = paginate(len(subscriptions), page, 5)
    subscriptions = subscriptions[metadata.start:metadata.end]
    await dialog_info(ctx, bot, state, text=await _("listSubscriptions"),
                      reply_markup=await InlineM.get_list_subscriptions_keyboard(metadata, subscriptions)
                      )


async def subscriptions_pagination(ctx: CallbackQuery, callback_data: PaginationCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, page=callback_data.page)


async def select_subscription(ctx: CallbackQuery, callback_data: SubscriptionCD, bot: Bot, state: FSMContext, vpn_client):
    await state.update_data(**{Fields.SubscriptionId: callback_data.sub_id})
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


# SUBSCRIPTION DEVICES LIST
async def subscriptions_devices_list(ctx, bot: Bot, state: FSMContext, vpn_client, page=1):
    data = await state.get_data()
    devices = await get_all_subscription_devices(data[Fields.SubscriptionId], vpn_client)
    metadata = paginate(len(devices), page, 5)
    devices = devices[metadata.start:metadata.end]
    await dialog_info(ctx, bot, state, text=await _("listDevices"),
                      reply_markup=await InlineM.get_list_subscription_devices_keyboard(metadata, devices)
                      )


async def subscriptions_devices_pagination(ctx: CallbackQuery, callback_data: PaginationCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, page=callback_data.page)


async def select_subscriptions_device(ctx: CallbackQuery, callback_data: DeviceCD, bot: Bot, state: FSMContext, vpn_client):
    await state.update_data(**{Fields.VpnDeviceId: callback_data.device_id})
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


# DEVICE DETAILS
async def device_vpn_details_information(ctx, bot: Bot, state: FSMContext, vpn_client):
    data = await state.get_data()
    vpn_item = await get_device_vpn_settings(data[Fields.VpnDeviceId], vpn_client)
    img_url = get_device_qrcode(data[Fields.VpnDeviceId])
    text = (await _("deviceVpnDetails")).format(
        img_url=img_url,
        private_key=vpn_item['private_key'],
        preshared_key=vpn_item['preshared_key'],
        allowed_ips=vpn_item['allowed_ips'],
        address=vpn_item['address'],
        dns=vpn_item['dns'],
        public_key=vpn_item['public_key'],
        endpoint=vpn_item['endpoint'],
    )
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_device_details_keyboard()
                      )


# Utility
async def prev(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.prev(ctx, bot, state, vpn_client=vpn_client)


async def account_subscription_entrypoint(ctx, bot, state: FSMContext, subscription_id, vpn_client):
    data = await state.get_data()
    await state.clear()
    await state.update_data(**{
        Fields.SubscriptionId: subscription_id,
        MessageType.Main: data[MessageType.Main]
    })
    await fsmPipeline.move_to(ctx, bot, state, StateF.UserSubscriptionDevices, vpn_client=vpn_client)


def setup(prev_menu):
    prev_inline = (NavCD.filter(F.type == NavType.BACK), prev)
    subscriptions_pagination_inline = (PaginationCD.filter(), subscriptions_pagination)
    subscription_devices_pagination_inline = (PaginationCD.filter(), subscriptions_devices_pagination)

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.AllUserSubscriptions, handler=select_subscription,
                         information=subscriptions_list,
                         filters=[SubscriptionCD.filter()],
                         inline_navigation_handler=[prev_menu, subscriptions_pagination_inline]
                         ),
        CallbackResponse(state=StateF.UserSubscriptionDevices, handler=select_subscriptions_device,
                         information=subscriptions_devices_list,
                         filters=[DeviceCD.filter()],
                         inline_navigation_handler=[prev_inline, subscription_devices_pagination_inline]
                         ),
        CallbackResponse(state=StateF.UserDeviceSubDetails, handler=prev,
                         information=device_vpn_details_information,
                         filters=[NavCD.filter()],
                         )
    ])