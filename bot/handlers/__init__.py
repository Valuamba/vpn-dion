from aiogram import Dispatcher

from handlers.commands import start


def setup(regular_router: Dispatcher):
    start.setup(regular_router)