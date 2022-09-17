import logging
from io import BytesIO

from aiogram import Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputFile, BufferedInputFile

from common.keyboard.utility_keyboards import NavCD, NavType
from handlers.account_subscriptions import StateF, Fields
from handlers.account_subscriptions.keyboard import InlineM, SubscriptionCD, DeviceCD, ConfigFileCD, DeviceTutorialCD, \
    DeviceTutorialType
from handlers.account_subscriptions.serivce import get_all_user_subscriptions, get_all_subscription_devices, \
    get_device_vpn_settings, get_device_qrcode, get_config_vpn, send_tutorial
from common.services.vpn_client_webapi import gettext as _
from utils.fsm.fsm_utility import dialog_info, MessageType
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.markup_constructor.pagination import paginate, PaginationCD
from utils.update import get_user_id

fsmPipeline = FSMPipeline()
logger = logging.getLogger(__name__)


# SUBSCRIPTIONS LIST
async def subscriptions_list(ctx, bot: Bot, state: FSMContext, vpn_client, page = 1):
    logger.info(f'User: {get_user_id(ctx)}. Info: subscription list')
    subscriptions = await get_all_user_subscriptions(get_user_id(ctx), vpn_client)
    metadata = paginate(len(subscriptions), page, 5)
    subscriptions = subscriptions[metadata.start:metadata.end]
    await dialog_info(ctx, bot, state, text=await _("listSubscriptions"),
                      reply_markup=await InlineM.get_list_subscriptions_keyboard(metadata, subscriptions)
                      )


async def subscriptions_pagination(ctx: CallbackQuery, callback_data: PaginationCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: subscription pagination {ctx.data}')
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, page=callback_data.page)


async def select_subscription(ctx: CallbackQuery, callback_data: SubscriptionCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: select subscription [{ctx.data}]')
    await state.update_data(**{Fields.SubscriptionId: callback_data.sub_id})
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


# SUBSCRIPTION DEVICES LIST
async def subscriptions_devices_list(ctx, bot: Bot, state: FSMContext, vpn_client, page=1):
    logger.info(f'User: {get_user_id(ctx)}. Info: subscription devices')
    data = await state.get_data()
    devices = await get_all_subscription_devices(data[Fields.SubscriptionId], vpn_client)
    metadata = paginate(len(devices), page, 5)
    devices = devices[metadata.start:metadata.end + 1]
    await dialog_info(ctx, bot, state, text=await _("listDevices"),
                      reply_markup=await InlineM.get_list_subscription_devices_keyboard(metadata, devices)
                      )


async def subscriptions_devices_pagination(ctx: CallbackQuery, callback_data: PaginationCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: subscription devices pagination {ctx.data}')
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, page=callback_data.page)


async def select_subscriptions_device(ctx: CallbackQuery, callback_data: DeviceCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: select subscription device {ctx.data}')
    await state.update_data(**{Fields.VpnDeviceId: callback_data.device_id})
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


# DEVICE DETAILS
async def device_vpn_details_information(ctx, bot: Bot, state: FSMContext, vpn_client, is_config_file_disabled = False):
    logger.info(f'User: {get_user_id(ctx)}. Info: device details.')
    data = await state.get_data()
    img_url = get_device_qrcode(data[Fields.VpnDeviceId])
    text = (await _("deviceVpnDetails")).format(
        img_url=img_url,
        # private_key=vpn_item['private_key'],
        # preshared_key=vpn_item['preshared_key'],
        # allowed_ips=vpn_item['allowed_ips'],
        # address=vpn_item['address'],
        # dns=vpn_item['dns'],
        # public_key=vpn_item['public_key'],
        # endpoint=vpn_item['endpoint'],
    )
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_device_details_keyboard(data[Fields.VpnDeviceId], is_config_file_disabled)
                      )


async def handle_get_config_file(ctx: CallbackQuery, callback_data: ConfigFileCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: config file {ctx.data}')
    data = await state.get_data()
    vpn_item = await get_device_vpn_settings(callback_data.device_id, vpn_client)
    config_b = await get_config_vpn(data[Fields.VpnDeviceId], vpn_client)
    # vpn_item = await get_device_vpn_settings(data[Fields.VpnDeviceId], vpn_client)
    # in_memory_pdf = BytesIO(bytes(response.body, 'ascii'))

    file = BufferedInputFile(file=config_b, filename=f"VPN ({vpn_item['country']}).conf")

    await bot.send_document(get_user_id(ctx), file)
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, is_config_file_disabled=True)


async def handle_device_tutorial(ctx: CallbackQuery, callback_data: DeviceTutorialCD, bot: Bot, state: FSMContext, vpn_client):
    if callback_data.type == DeviceTutorialType.WINDOWS:
        await send_tutorial('windows', 'windowsTutorial', bot, ctx)
    elif callback_data.type == DeviceTutorialType.IOS:
        await send_tutorial('ios/default', 'iosTutorialDefault', bot, ctx)
        await send_tutorial('ios/killswitch', 'iosTutorialKillSwitch', bot, ctx)
    elif callback_data.type == DeviceTutorialType.ANDROID:
        await send_tutorial('android', 'androidTutorial', bot, ctx)
    elif callback_data.type == DeviceTutorialType.LINUX:
        await send_tutorial('linux', 'linuxTutorial', bot, ctx)
    elif callback_data.type == DeviceTutorialType.MACOS:
        await send_tutorial('macOs/default', 'macOsTutorialDefault', bot, ctx)
        await send_tutorial('macOs/killswitch', 'macOsTutorialKillSwitch', bot, ctx)
    elif callback_data.type == DeviceTutorialType.SMART_TV:
        await send_tutorial('smartTv/bridge', 'smartTVBridgeTutorial', bot, ctx)
        await send_tutorial('smartTv/vpn', 'smartTVVpnTutorial', bot, ctx)
        await send_tutorial('smartTv/4k', 'smartTV4kTutorial', bot, ctx)


# Utility
async def prev(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state: FSMContext, vpn_client):
    await fsmPipeline.prev(ctx, bot, state, vpn_client=vpn_client)


async def account_subscription_entrypoint(ctx, bot, state: FSMContext, subscription_id, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Entrypoint: subscription {ctx.data}')
    data = await state.get_data()
    await state.clear()
    await state.update_data(**{
        Fields.SubscriptionId: subscription_id,
        MessageType.Main: data[MessageType.Main]
    })
    await fsmPipeline.move_to(ctx, bot, state, StateF.UserSubscriptionDevices, vpn_client=vpn_client)


async def redirect_to_sub_devices_info(ctx, bot, state, vpn_client, subscription_id):
    await state.update_data(**{Fields.SubscriptionId: subscription_id})
    await fsmPipeline.move_to(ctx, bot, state, StateF.UserSubscriptionDevices, vpn_client=vpn_client)


def setup(prev_menu):
    prev_inline = (NavCD.filter(F.type == NavType.BACK), prev)
    subscriptions_pagination_inline = (PaginationCD.filter(), subscriptions_pagination)
    subscription_devices_pagination_inline = (PaginationCD.filter(), subscriptions_devices_pagination)
    download_config_inline = (ConfigFileCD.filter(), handle_get_config_file)
    device_tutorial_inline = (DeviceTutorialCD.filter(), handle_device_tutorial)

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
                         inline_navigation_handler=[download_config_inline, device_tutorial_inline]
                         )
    ])