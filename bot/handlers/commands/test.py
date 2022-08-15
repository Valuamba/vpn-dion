from aiogram import Dispatcher, Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, LabeledPrice

from handlers.process_subscription import view_payment, ProcessSubscriptionStateGroup
from utils.update import get_chat_id


async def command_info(ctx: Message, bot: Bot, state: FSMContext):
    await bot.send_message(get_chat_id(ctx), "hehe",
                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                               [InlineKeyboardButton(text="Some", web_app=WebAppInfo(url="https://a9d6-178-120-63-202.eu.ngrok.io/payment/"))]
                           ]))
    # await state.clear()
    # await view_payment.fsmPipeline.move_to(ctx, bot, state, moved_state=ProcessSubscriptionStateGroup.SelectPaymentMethod)


async def create_checkout(ctx: Message, bot: Bot, state: FSMContext):
    text = '''
⚖️ Выбранный тариф:
\n\n
🗓 3 месяца 📱 2 устройства: 2640 ₽ (🔻69.00%)
\n\n
💳 К оплате: 2587.00 ₽ (без скидок 8400.00 ₽)
'''
    await bot.send_invoice(get_chat_id(ctx),
                           title='VPN подписка',
                           description='Тариф: 🗓 3 месяца 📱 2 устройства 🔻69%',
                           payload='123',
                           provider_token='381764678:TEST:40401',
                           currency='RUB',
                           prices=[
                               LabeledPrice(label='📱 Antigua and Barbuda', amount=130000),
                               LabeledPrice(label='📱 Belarus 🔻 20%', amount=1300000),
                               LabeledPrice(label='📱 Norway', amount=250000),
                               LabeledPrice(label='📱 USA', amount=50000),
                               LabeledPrice(label='📱 Germany', amount=12222),
                           ]
                           )


def setup(dp: Dispatcher):
    dp.message.register(command_info, commands="test")
    dp.message.register(create_checkout, commands="payment")
    view_payment.setup()
    view_payment.fsmPipeline.build(dp)
