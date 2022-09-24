
from aiogram.filters.callback_data import CallbackData

from common.keyboard.utility_keyboards import NavCD, NavType
from common.services.vpn_client_webapi import gettext
from handlers.reviews.paginator import InlineKeyboardPaginator
from utils.markup_constructor import InlineMarkupConstructor
from utils.markup_constructor.refactor import refactor_keyboard


class MultiPagePaginationCD(CallbackData, prefix='multi-page'):
    number: str


class ReviewsInlineMarkup(InlineMarkupConstructor):

    async def get_pag_keyboard(self, *, page, array_count: int):
        paginator = InlineKeyboardPaginator(
            array_count,
            current_page=page
        )
        paginator.add_after([{'text': await gettext("back"), 'callback_data': NavCD(type=NavType.BACK).pack()}])

        return paginator.get_markup(after_schema=[1])


InlineM = ReviewsInlineMarkup()
