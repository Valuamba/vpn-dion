import logging

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Update, FSInputFile
from aiogram.utils.markdown import hcode

from config import Config
from utils.broadcast import from_iterable, broadcast_smth
from utils.update import get_chat_id_from_update


async def errors_handler(update: Update, exception, state: FSMContext, bot: Bot, user_db):
    notify_user = True
    data = await state.get_data()
    state = await state.get_state()
    if isinstance(exception, TelegramBadRequest):
        if "Bad Request: message is not modified:" in exception.message:
            notify_user = False
    # text = "Вызвано необрабатываемое исключение. Администратор был уведомлен об ошибке.\n"

    kwargs = {
        **data,
        'state': state,
    }

    user_data = '\n'.join(f'{k}: {v}' for k,v in kwargs.items())
    error_caption = f"{hcode(f'Chat id: {get_chat_id_from_update(update)} Error: {type(exception)}: {exception}')}"

    error = f'Error: {type(exception)}: {exception}'
    document_path = Config.LOG_FILE_PATH
    logging.exception(error)
    users = from_iterable(Config.DEVELOPER_TG_ID)
    await broadcast_smth(users, bot.send_document, False, document=FSInputFile(path=document_path, filename="log"),
                                caption=f'{user_data}\n{error_caption}')

    # if notify_user:
    #     await bot.send_message(chat_id=get_chat_id_from_update(update), text=f"{text}")


def setup(dp: Dispatcher):
    dp.errors.register(errors_handler)
