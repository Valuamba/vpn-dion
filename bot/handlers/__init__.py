from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from magic_filter import F

from common.filters import group_filter
from common.filters.group_filter import GroupFilter
from handlers import inline
from handlers.global_handlers import handlers as global_handlers
from handlers.commands import start, test
from handlers.catcher import handler as catcher
# from aiogram.exceptions import Te


# @dp.errors_handler(exception=MessageNotModified)
# async def message_not_modified(*_):
#     return True


def setup(regular_router: Dispatcher):
    regular_router.message.filter(GroupFilter())

    global_handlers.setup(regular_router)
    inline.setup(regular_router)
    start.setup(regular_router)
    test.setup(regular_router)

    # regular_router.errors.handlers(message_not_modified, F.exception=)
    catcher.setup(regular_router)

    # regular_router.shipping_query.register()