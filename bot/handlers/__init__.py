from aiogram import Dispatcher

from handlers.commands import start, test


def setup(regular_router: Dispatcher):
    start.setup(regular_router)
    test.setup(regular_router)

    # regular_router.shipping_query.register()