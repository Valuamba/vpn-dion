import logging

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.methods import send_message
from aiogram.types import CallbackQuery

from common.keyboard.utility_keyboards import NavCD, NavType
from common.morph import get_morph
from common.services.vpn_client_webapi import gettext
from handlers.account_subscriptions.serivce import get_all_user_subscriptions
from handlers.account_subscriptions.view import redirect_to_sub_devices_info
from handlers.referral import StateF, Fields
from handlers.referral.keyboard import InlineM, ReferralCD, ReferralButtonType
from handlers.referral.service import get_user_referral_data, activate_free_month_subscription
from utils.fsm.fsm_utility import dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.update import get_user_id

fsmPipeline = FSMPipeline()
logger = logging.getLogger(__name__)


'''
REFERRAL INFO
'''


async def referral_info(ctx, bot, state, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. See referral info')
    referral_data = await get_user_referral_data(get_user_id(ctx), vpn_client)
    text = (await gettext('referralProgramInfo')).format(
        referral_link=referral_data['referral_link'],
        count_referrals=referral_data['count_referrals'],
        count_free_month=referral_data['count_free_month_subscription']
    )
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_referral_keyboard(referral_data['count_free_month_subscription']))


async def handle_referral_button(ctx: CallbackQuery, callback_data: ReferralCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler referral button {ctx.data}')
    if callback_data.type == ReferralButtonType.GET_REWARD:
        active_subscriptions = await get_all_user_subscriptions(get_user_id(ctx), vpn_client)
        if len(active_subscriptions) > 0:
            await fsmPipeline.move_to(ctx, bot, state, StateF.AcceptGettingReward, vpn_client=vpn_client)
        else:
            activated_data = await activate_free_month_subscription(get_user_id(ctx), vpn_client)
            await state.update_data(**{
                Fields.ActivatedMonthCount: activated_data['month_duration'],
                Fields.ActivatedSubscriptionId: activated_data['subscription_id']
            })
            await fsmPipeline.move_to(ctx, bot, state, StateF.ActivatedFreeSubInfo, vpn_client=vpn_client)


# SUB DIALOG
async def free_sub_navigation_dialog(ctx, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Info sub navigation dialog')
    text = await gettext('activeSubscriptionAlreadyExist')
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_dialog_keyboard())


async def free_sub_dialog_handle(ctx: CallbackQuery, callback_data: NavCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler free sub navigation {ctx.data}')
    if callback_data.type == NavType.YES:
        activated_data = await activate_free_month_subscription(get_user_id(ctx), vpn_client)
        await state.update_data(**{
            Fields.ActivatedMonthCount: activated_data['month_duration'],
            Fields.ActivatedSubscriptionId: activated_data['subscription_id']
        })
        await fsmPipeline.move_to(ctx, bot, state, StateF.ActivatedFreeSubInfo, vpn_client=vpn_client)


# ACTIVATED SUB

async def activated_subscription_info(ctx, bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Info activate subscription')
    data = await state.get_data()
    activated_month = data[Fields.ActivatedMonthCount]
    subscription_id = data[Fields.ActivatedSubscriptionId]
    text = (await gettext('getFreeMonth')).format(
        month_c=data[Fields.ActivatedMonthCount],
        month_loc=get_morph('месяц', activated_month)
    )
    await dialog_info(ctx, bot, state, text=text, reply_markup=await InlineM.get_activated_keyboard(subscription_id))


async def activated_sub_handler(ctx: CallbackQuery, callback_data: ReferralCD, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler activate subscription {ctx.data}')
    if callback_data.type == ReferralButtonType.SEE_SUBSCRIPTION:
        await redirect_to_sub_devices_info(ctx, bot, state, vpn_client, callback_data.sub_id)


def setup(prev_menu):

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.ReferralMenu, handler=handle_referral_button,
                         information=referral_info,
                         filters=[ReferralCD.filter()],
                         inline_navigation_handler=[prev_menu]),
        CallbackResponse(state=StateF.AcceptGettingReward, handler=free_sub_dialog_handle,
                         information=free_sub_navigation_dialog,
                         filters=[NavCD.filter()],
                         inline_navigation_handler=[prev_menu]
                         ),
        CallbackResponse(state=StateF.ActivatedFreeSubInfo, handler=activated_sub_handler,
                         information=activated_subscription_info,
                         filters=[ReferralCD.filter()],
                         inline_navigation_handler=[prev_menu]
                         ),
    ])