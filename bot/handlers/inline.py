from aiogram import Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputMessageContent, InputTextMessageContent

from common.services.vpn_client_webapi import gettext, get_locales
from handlers.referral.service import get_user_referral_data


async def get_vpn_info(inline_query: InlineQuery, bot: Bot, state: FSMContext, vpn_client):
    ref_data = await get_user_referral_data(inline_query.from_user.id, vpn_client)
    locales = await get_locales('suggestVpnBotInline', 'suggestVPNBot')
    text = locales['suggestVPNBot'].format(referral_link=ref_data['referral_link'])
    await bot.answer_inline_query(inline_query.id,
                                  results=[InlineQueryResultArticle(id=1, title=locales['suggestVpnBotInline'],
                                                                    input_message_content=InputTextMessageContent(message_text=text),
                                                                    description=text)])


def setup(dp: Dispatcher):
    dp.inline_query.register(get_vpn_info)