import logging

from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, Update, TelegramObject

from common.keyboard.global_markup import GlobalKeyboardMarkup
from common.morph import morph, get_morph, get_accs_morph
from common.services.vpn_client_webapi import update_user, gettext, activate_invited_user_subscription
from handlers.menu import view as menuView, MenuStatesGroup
from utils.update import get_user_id


logger = logging.getLogger(__name__)


async def command_info(ctx: Message, context, bot: Bot, state: FSMContext, user_db, vpn_client):
    logger.info(f'User: {get_user_id(ctx)}. Command: start.')
    await state.clear()
    # Могут быть проблемы нагрузки в будущем.
    # Лучше прокинуть через middleware поле Update и таким образом получать.
    # await state.update_data({ 'update_id': context['update_id']})
    await menuView.fsmPipeline.move_to(ctx, bot, state, moved_state=MenuStatesGroup.Menu, vpn_client=vpn_client)

    if user_db.get('is_first_creation', None) and user_db.get('referral_item_id', None):
        result = await activate_invited_user_subscription(get_user_id(ctx), vpn_client, days_duration=7)
        text = (await gettext('freeReferralPeriod')).format(
            duration=1,
            duration_loc=get_accs_morph('неделя', 1)
        )
        await bot.send_message(get_user_id(ctx), text, reply_markup=await GlobalKeyboardMarkup().get_nav_to_sub_details(result['subscription_id']))


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="start")
    menuView.setup()
    menuView.fsmPipeline.build(dp)
