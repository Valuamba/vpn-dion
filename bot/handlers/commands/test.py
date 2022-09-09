import os
import re

from aiogram import Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, LabeledPrice, \
    InputMediaPhoto, InputFile, FSInputFile

from common.services.vpn_client_webapi import gettext
from config import Config
# from handlers.process_subscription import view_payment, ProcessSubscriptionStateGroup
from utils.update import get_chat_id


def absoluteFilePats(directory):
    for dirpath,_,filenames in os.walk(directory):
        sorted_files = sorted(filenames, key=lambda f: int(re.match('\d+(?<!.jpg)', f).group(0)), reverse=False)
        for file_name in sorted_files:
            yield os.path.abspath(os.path.join(dirpath, file_name))


async def send_tutorial(sub_directory, alias, bot, ctx):
    text = await gettext(alias)
    medias = [InputMediaPhoto(media=FSInputFile(path=m)) for m in
              absoluteFilePats(os.path.join(Config.BASE_DIR, 'bot/common/assets', sub_directory))]
    if len(medias) > 8:
        first_part = medias[:8]
        second_part = medias[8:]
        await bot.send_media_group(get_chat_id(ctx), media=first_part)
        await bot.send_media_group(get_chat_id(ctx), media=second_part)
    elif len(medias) > 0:
        await bot.send_media_group(get_chat_id(ctx), media=medias)
        await bot.send_message(get_chat_id(ctx), text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(get_chat_id(ctx), text=text, disable_web_page_preview=True)


async def command_info(ctx: Message, bot: Bot, state: FSMContext):
    tutorial_type = 'smarttv'

    if tutorial_type == 'android':
        await send_tutorial('android', 'androidTutorial', bot, ctx)
    elif tutorial_type == 'ios':
        await send_tutorial('ios/default', 'iosTutorialDefault', bot, ctx)
        await send_tutorial('ios/killswitch', 'iosTutorialKillSwitch', bot, ctx)
    elif tutorial_type == 'macos':
        await send_tutorial('macOs/default', 'macOsTutorialDefault', bot, ctx)
        await send_tutorial('macOs/killswitch', 'macOsTutorialKillSwitch', bot, ctx)
    elif tutorial_type == 'smarttv':
        await send_tutorial('smartTv/bridge', 'smartTVBridgeTutorial', bot, ctx)
        await send_tutorial('smartTv/vpn', 'smartTVVpnTutorial', bot, ctx)
        await send_tutorial('smartTv/4k', 'smartTV4kTutorial', bot, ctx)


    # await bot.send_message(get_chat_id(ctx), "hehe",
    #                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
    #                            [InlineKeyboardButton(text="Some", web_app=WebAppInfo(url="https://5b1f-37-214-31-225.eu.ngrok.io/web/?subscription_id=6&state=ExtendVpnSubscription"))]
    #                        ]))
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
    # dp.message.register(create_checkout, commands="payment")
    # view_payment.setup()
    # view_payment.fsmPipeline.build(dp)
