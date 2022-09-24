import logging
from typing import Any

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto, CallbackQuery

from utils.fsm.fsm_utility import MessageType
from utils.update import get_chat_id

logger = logging.getLogger(__name__)


async def remove_window_message(ctx: Any, bot: Bot, state: FSMContext):
    data = await state.get_data()

    message_key = next((k for k, v in data.items() if k.endswith(MessageType.Window)), None)
    if message_key:
        message_id = data[message_key]
        if message_id:
            await bot.delete_message(get_chat_id(ctx), message_id=message_id)
            await state.update_data({message_key: None})


async def window_info(ctx: Any, bot: Bot, state: FSMContext, *, prefix: str, **func_kwargs):
    '''
    text, reply_markup, data, media
    '''

    message_key = '{prefix}_' + MessageType.Window

    data = func_kwargs.get('data', await state.get_data())
    func_kwargs['data'] = data

    chat_id = get_chat_id(ctx)
    main_message_id = data.get(message_key, None)

    bot_kwargs = func_kwargs
    bot_kwargs.pop('data', None)
    bot_kwargs.pop(message_key, None)

    if main_message_id:
        try:
            await edit_main_message(chat_id, main_message_id, bot, **bot_kwargs)
        except Exception as exception:
            if isinstance(exception, TelegramBadRequest):
                if "Bad Request: message is not modified:" in exception.message:
                    logger.warning("Bad Request: message is not modified:")
                    if isinstance(ctx, CallbackQuery):
                        await ctx.answer()
                    return

            raise
    else:
        await send_main_message(ctx, bot, state, prefix=prefix, **bot_kwargs)


async def edit_main_message(chat_id, main_message_id, bot: Bot, **func_kwargs):
    text: str = func_kwargs.get('text', None)
    if text:
        await bot.edit_message_text(message_id=main_message_id, chat_id=chat_id, parse_mode='HTML',
                                    **func_kwargs)
    elif func_kwargs.get('media', None):
        await bot.edit_message_media(message_id=main_message_id, chat_id=chat_id, **func_kwargs)
    elif func_kwargs.get('photo', None):
        media = InputMediaPhoto(media=func_kwargs.pop('photo'), caption=func_kwargs.pop('caption'))
        func_kwargs['media'] = media
        await bot.edit_message_media(message_id=main_message_id, chat_id=chat_id, **func_kwargs)
    else:
        raise Exception('There is no text or media arguments')


async def send_main_message(ctx: Any, bot: Bot, state: FSMContext, *, prefix: str, **func_kwargs):
    message_key = '{prefix}_' + MessageType.Window
    if 'photo' in func_kwargs:
        message = await bot.send_photo(chat_id=get_chat_id(ctx), **func_kwargs)
    else:
        message = await bot.send_message(chat_id=get_chat_id(ctx), parse_mode='HTML',
                                     **func_kwargs)
    await state.update_data(**{message_key: message.message_id})