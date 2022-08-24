from aiogram import Dispatcher

from handlers import inline
from handlers.commands import start, test


def setup(regular_router: Dispatcher):
    inline.setup(regular_router)
    start.setup(regular_router)
    test.setup(regular_router)

    # regular_router.shipping_query.register()