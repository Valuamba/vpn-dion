from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from handlers import inline
from handlers.global_handlers import handlers as global_handlers
from handlers.commands import start, test


# def clb(ctx: CallbackQuery, callback_data, bot, state):
#     pass

def setup(regular_router: Dispatcher):

    # regular_router.callback_query.register(clb)

    global_handlers.setup(regular_router)
    inline.setup(regular_router)
    start.setup(regular_router)
    test.setup(regular_router)

    # regular_router.shipping_query.register()