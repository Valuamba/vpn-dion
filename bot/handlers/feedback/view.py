import logging

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common.services.vpn_client_webapi import gettext, add_feedback_message
from config import Config
from handlers.feedback import StateF
from handlers.feedback.keyboard import InlineM
from utils.fsm.fsm_utility import dialog_info, send_main_message
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import ResponseTextMessage, CallbackResponse
from utils.update import get_user_id

fsmPipeline = FSMPipeline()
logger = logging.getLogger(__name__)


async def handle_feedback_message(ctx: Message, bot: Bot, state: FSMContext, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Handler: feedback message.')
    text = (await gettext('feedBackMessageChatAlias')).format(id=get_user_id(ctx), text=ctx.text)
    await bot.send_message(Config.ADMINISTRATION_CHAT_ID, text)
    await add_feedback_message(get_user_id(ctx), ctx.message_id, ctx.text, vpn_client)
    await fsmPipeline.next(ctx, bot, state, vpn_client=vpn_client)


async def feedback_info(ctx, bot, state, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Info: feedback.')
    text = await gettext('menuHelp')
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_feedback_keyboard())


# AFTER SENDING

async def success_send_info(ctx, bot, state, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Info: success send help message..')
    text = await gettext('successSendHelpMessage')
    await send_main_message(ctx, bot, state, text=text,
                            reply_markup=await InlineM.get_success_keyboard()
                            )


def setup(menu_prev):
    fsmPipeline.set_pipeline([
        ResponseTextMessage(state=StateF.WriteFeedBackMessage, handler=handle_feedback_message,
                            information=feedback_info,
                            inline_navigation_handler=[menu_prev]),
        CallbackResponse(state=StateF.SuccessSendingHelp, handler=menu_prev[1],
                         filters=[menu_prev[0]],
                         information=success_send_info
                         ),
    ])