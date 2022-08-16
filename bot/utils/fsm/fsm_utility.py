from enum import Enum
from typing import Any, List, Optional, Dict
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, InputMedia, MessageEntity

from utils.fsm.step_types import MAIN_STEP_MESSAGE_ID, UTILITY_MESSAGE_IDS
from utils.update import get_chat_id


class MessageType:
    Main = "main_message_id"
    Utility = "utility_message_id"
    Form = "form_message_id"


class StepInfoType(Enum):
    Main = 1,
    Utility = 2


async def add_utility_msg(msg: Message, state: FSMContext):
    data = await add_item_list(state, msg.message_id, MessageType.Utility)
    await state.update_data(data)


async def add_item_list(state, item, key) -> dict:
    data = await state.get_data()
    array = data.get(key, [])
    if item in array:
        array.remove(item)
    else:
        array.append(item)
    data[key] = array
    return data


async def dialog_info(ctx: Any, bot: Bot, state: FSMContext, **func_kwargs):
    '''
    text, reply_markup, data, media
    '''

    data = func_kwargs.get('data', await state.get_data())
    func_kwargs['data'] = data

    chat_id = get_chat_id(ctx)
    main_message_id = data.get(MessageType.Main, None)

    bot_kwargs = func_kwargs
    bot_kwargs.pop('data', None)
    bot_kwargs.pop(MessageType.Main, None)

    if main_message_id:
        await edit_main_message(chat_id, main_message_id, bot, **bot_kwargs)
    else:
        await send_main_message(ctx, bot, state, **bot_kwargs)


async def edit_main_message(chat_id, main_message_id, bot: Bot, **func_kwargs):
    text: str = func_kwargs.get('text', None)
    if text:
        await bot.edit_message_text(message_id=main_message_id, chat_id=chat_id, parse_mode='HTML',
                                    **func_kwargs)
    elif func_kwargs.get('media', None):
        await bot.edit_message_media(message_id=main_message_id, chat_id=chat_id, **func_kwargs)
    else:
        raise Exception('There is no text or media arguments')


async def send_main_message(ctx: Any, bot: Bot, state: FSMContext, **func_kwargs):
    message = await bot.send_message(chat_id=get_chat_id(ctx), parse_mode='HTML',
                                     **func_kwargs)
    await state.update_data(**{MessageType.Main: message.message_id})


async def send_utility_message(ctx: Any, bot: Bot, state: FSMContext, text: str, reply_markup=None, disable_notification: Optional[bool]=None):
    message = await bot.send_message(chat_id=get_chat_id(ctx), text=text, parse_mode='HTML',
                                     reply_markup=reply_markup, disable_notification=disable_notification
                                     )
    await add_utility_msg(message, state)


async def step_info(ctx: Any, state: FSMContext, bot: Bot, text, reply_markup=None, step_info_type=StepInfoType.Main,
                    update_type: Any = None, disable_notification: Optional[bool]=None):
    data = await state.get_data()
    main_step_message = data.get(MAIN_STEP_MESSAGE_ID, None)

    async def main_message():
        message = await bot.send_message(chat_id=get_chat_id(ctx), text=text, parse_mode='HTML',
                                         reply_markup=reply_markup, disable_notification=disable_notification
                                         )
        data[MAIN_STEP_MESSAGE_ID] = message.message_id
        await state.update_data(data)

    async def utility_message():
        message = await bot.send_message(chat_id=get_chat_id(ctx), text=text, parse_mode='HTML',
                                         reply_markup=reply_markup, disable_notification=disable_notification
                                         )
        utility_ids = await add_item_list(state, message.message_id, UTILITY_MESSAGE_IDS)
        await state.update_data(**{UTILITY_MESSAGE_IDS: utility_ids})

    async def message_switch():
        if step_info_type == StepInfoType.Main:
            await main_message()
        elif step_info_type == StepInfoType.Utility:
            await utility_message()
        else:
            raise Exception(f'Step info type {step_info_type} doesent supported')

    async def callback_switch():
        if step_info_type == StepInfoType.Main:
            await bot.edit_message_text(chat_id=get_chat_id(ctx), message_id=main_step_message, parse_mode='HTML', text=text,
                                        reply_markup=reply_markup)
        elif step_info_type == StepInfoType.Utility:
            await bot.edit_message_text(chat_id=get_chat_id(ctx), message_id=ctx.message.message_id,
                                        parse_mode='HTML', text=text,
                                        reply_markup=reply_markup
                                        )

    if update_type == Message:
        await message_switch()
    elif main_step_message and update_type == CallbackQuery:
        await callback_switch()
    elif isinstance(ctx, Message):
        await message_switch()
    elif main_step_message and isinstance(ctx, CallbackQuery):
        await callback_switch()
    elif not main_step_message:
        await message_switch()
    else:
        raise Exception(f'Step info type {step_info_type} doesent supported')