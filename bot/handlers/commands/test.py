from aiogram import Dispatcher, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message

from handlers.process_subscription import view_payment, ProcessSubscriptionStateGroup


async def command_info(ctx: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await view_payment.fsmPipeline.move_to(ctx, bot, state, moved_state=ProcessSubscriptionStateGroup.SelectPaymentMethod)


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="test")
    view_payment.setup()
    view_payment.fsmPipeline.build(dp)
