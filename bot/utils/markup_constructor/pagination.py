import math
from enum import IntEnum
from typing import Any, Tuple, List, Coroutine, Union

from aiogram.filters.callback_data import CallbackData
from beanie.odm.queries.find import FindMany
from pydantic import BaseModel

from utils.markup_constructor import InlineMarkupConstructor


class PagintaionType(IntEnum):
    Next = 1
    Prev = -1
    Page = 2,
    Empty = 1


class PaginationCD(CallbackData, prefix='pagination'):
    pag_type: PagintaionType
    page: int = None


class PaginationMetadata:
    def __init__(self, total, curr, start, end, prev_page, next_page):
        self.total = total
        self.curr = curr
        self.start = start
        self.end = end
        self.prev_page = prev_page
        self.next_page = next_page


class PaginationInline(InlineMarkupConstructor):
    def get_pagination_keyboard(self, actions: [], schema: [], metadata: PaginationMetadata):
        pag = []
        if metadata.prev_page or metadata.next_page:
            if metadata.prev_page:
                pag.append({ 'text': 'Назад', 'callback_data': PaginationCD(pag_type=PagintaionType.Prev, page=metadata.prev_page).pack()})
            else:
                pag.append({ 'text': ' ', 'callback_data': PaginationCD(pag_type=PagintaionType.Empty).pack()})

            pag.append({ 'text': metadata.curr, 'callback_data': PaginationCD(pag_type=PagintaionType.Page).pack()})

            if metadata.next_page:
                pag.append({ 'text': 'Далее', 'callback_data': PaginationCD(pag_type=PagintaionType.Next, page=metadata.next_page).pack()})
            else:
                pag.append({ 'text': ' ', 'callback_data': PaginationCD(pag_type=PagintaionType.Empty).pack()})

            actions += pag
            schema.append(3)


def paginate(total_items: int, current_page: int = 1, page_size: int = 10):

    if total_items == 0:
        return PaginationMetadata(total=total_items, curr=current_page, start=0, end=0,
                                  prev_page=0, next_page=0
                                  )

    total_pages = math.ceil(total_items / page_size)
    next_page = None
    prev_page = None

    if current_page < 1:
        current_page = 1
    elif current_page > total_pages:
        current_page = total_pages

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size - 1, total_items)

    if current_page != total_pages:
        next_page = current_page + 1

    if current_page != 1:
        prev_page = current_page - 1

    return PaginationMetadata(total=total_items, curr=current_page, start=start_index, end=end_index,
                              prev_page=prev_page, next_page=next_page)


MONGO_TYPE = List[Union[BaseModel, Any]]


async def paginate_query_async(query: FindMany[Any], page: int, max: int) -> Tuple[MONGO_TYPE, PaginationMetadata]:
    total = await query.count()
    metadata = paginate(total, page, max)

    results = await query.skip(metadata.start).limit(
        metadata.end - metadata.start + 1
    ).to_list()

    return results, metadata

