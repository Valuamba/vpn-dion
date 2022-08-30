from aiogram import Dispatcher

from handlers import inline
from handlers.global_handlers import handlers as global_handlers
from handlers.commands import start, test


def setup(regular_router: Dispatcher):
    global_handlers.setup(regular_router)
    inline.setup(regular_router)
    start.setup(regular_router)
    test.setup(regular_router)

    # regular_router.shipping_query.register()