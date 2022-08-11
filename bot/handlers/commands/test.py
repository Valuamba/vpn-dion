from aiogram import Dispatcher, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from handlers.process_subscription import view_payment, ProcessSubscriptionStateGroup
from utils.update import get_chat_id


async def command_info(ctx: Message, bot: Bot, state: FSMContext):
    await bot.send_message(get_chat_id(ctx), "hehe",
                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text="Some", web_app=WebAppInfo(url="https://8714-178-120-63-202.eu.ngrok.io/payment/"))]
                           ]))
    # await state.clear()
    # await view_payment.fsmPipeline.move_to(ctx, bot, state, moved_state=ProcessSubscriptionStateGroup.SelectPaymentMethod)


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="test")
    view_payment.setup()
    view_payment.fsmPipeline.build(dp)
