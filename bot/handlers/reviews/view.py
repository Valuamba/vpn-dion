import itertools
import os

from aiogram import Bot
from aiogram.types import CallbackQuery, InlineKeyboardButton, InputMediaPhoto, FSInputFile

from config import Config
from handlers.reviews import StateF
from handlers.reviews.keyboard import InlineM, MultiPagePaginationCD
from handlers.reviews.page_pagination import paginate
from handlers.reviews.paginator import InlineKeyboardPaginator, PaginatorCD
from utils.fsm.fsm_utility import dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse
from utils.fsm.window_utility import window_info
from utils.str import absolute_file_paths
from utils.update import get_chat_id

fsmPipeline = FSMPipeline()
WINDOW_PREFIX = 'review'


async def info(ctx, bot: Bot, state, vpn_client, page = 1):
    paths = absolute_file_paths(os.path.join(Config.ROOT_DIR, 'common/assets', 'reviews'))
    review_photo_path = next(itertools.islice(paths, page - 1, None))

    await window_info(ctx, bot, state, prefix=WINDOW_PREFIX,
                      photo=FSInputFile(path=review_photo_path), caption="Some caption",
                      reply_markup=await InlineM.get_pag_keyboard(page=page, array_count=sum(1 for _ in paths)))


async def handler(ctx: CallbackQuery, bot, state, vpn_client):
    pass


async def pag_handler(ctx: CallbackQuery, callback_data: PaginatorCD, bot, state, vpn_client):
    await fsmPipeline.info(ctx, bot, state, vpn_client=vpn_client, page=int(callback_data.page))


def setup(prev_menu):
    pag_inline = (PaginatorCD.filter(), pag_handler)
    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.SeeReviews, handler=handler,
                         information=info,
                         inline_navigation_handler=[pag_inline, prev_menu]
                         )
    ])