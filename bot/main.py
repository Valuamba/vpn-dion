import logging
from aiogram import Bot, Dispatcher, Router
import i18n
import os

import handlers
from common import middlewares
from config import Config
from utils import logger
from utils.db import MyBeanieMongo
from utils.db.mongo_storage import MongoStorage
# from utils.set_bot_commands import set_commands


async def main():
    bot = Bot(token=Config.BOT_TOKEN, parse_mode='HTML')
    storage = MongoStorage.from_url(
        Config.MONGODB_URI,
        f"{Config.MONGODB_DATABASE}",
    )
    dp = Dispatcher(storage=storage)

    regular = Router()
    dp.include_router(regular)

    middlewares.setup(dp)
    handlers.setup(regular)

    logger.setup_logger()

    mongo = MyBeanieMongo()
    await mongo.init_db()

    # await notify_superusers(bot)
    # await set_commands(bot)
    # await update_message_locales()

    try:
        await dp.start_polling(bot)
    finally:
        logging.warning("Shutting down..")
        await bot.session.close()
        storage.close()
        await mongo.close()
        logging.warning("Bye!")
