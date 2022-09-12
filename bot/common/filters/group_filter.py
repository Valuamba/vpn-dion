from typing import Optional, Union, Literal, Dict, Any, List

from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, TelegramObject


class GroupFilter(BaseFilter):
    async def __call__(self, obj: TelegramObject, state: FSMContext) -> bool:
        return obj.chat.id == obj.from_user.id
