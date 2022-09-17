import asyncio
from typing import cast, AsyncGenerator, Iterable

from aiogram import types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from common.services.vpn_client_webapi import get_active_users
from handlers.broadcast.inline import CancelKb, CancelCD
from handlers.broadcast.states import BroadcastAdmin
from utils.broadcast import broadcast_smth
from utils.fsm.fsm_utility import dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse, ResponseTextMessage
from utils.update import get_chat_id

fsmPipeline = FSMPipeline()


async def start_broadcast(ctx, bot, state, vpn_client):
    await state.set_state(BroadcastAdmin.BROADCAST)
    await dialog_info(ctx, bot, state, text='Введите сообщение, которое хотели бы отправить всем, кто есть в базе:',
                     reply_markup=CancelKb().get())


async def start_broadcasting(msg: Message, bot: Bot, state: FSMContext, vpn_client):
    info_msg = await msg.answer("Рассылка запущена.")
    chats = from_iterable([chat['user_id'] for chat in await get_active_users(vpn_client)])

    async def send_copy(chat_id: int, count: int, message: Message, red_msg: Message) -> int:
        try:
            await message.send_copy(chat_id)

        except Exception as e:
            # user = await UserModel.find_one(UserModel.id == chat_id)
            # user.status = "left"
            # await user.save()
            raise e

        count += 1
        if count % 10 == 0:
            await red_msg.edit_text(f"Отправлено {count} сообщений.")
        return count

    amount = await broadcast_smth(
        cast(AsyncGenerator, chats), send_copy, True, message=msg, red_msg=info_msg
    )

    await info_msg.edit_text(f"Рассылка завершена. Отправлено {amount} сообщений.")


async def from_iterable(it: Iterable) -> AsyncGenerator:
    for item in it:
        await asyncio.sleep(0)
        yield item


def setup(prev_inline):
    # cancel_inline = (CancelCD.filter(), prev_inline)
    fsmPipeline.set_pipeline([
        ResponseTextMessage(state=BroadcastAdmin.BROADCAST, handler=start_broadcasting,
                            information=start_broadcast,
                            inline_navigation_handler=[prev_inline]
                            ),
        ]
    )