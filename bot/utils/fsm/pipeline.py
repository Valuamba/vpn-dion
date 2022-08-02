from __future__ import annotations

import asyncio
from enum import Enum, IntEnum
from itertools import chain
from typing import Union, Any, List, Optional, Iterable, Tuple, Type
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.dispatcher.event.handler import HandlerType, FilterType, FilterObject
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiohttp import ClientSession

from utils.fsm.fsm_utility import MessageType
from utils.fsm.step_types import ResponseTextMessage, CallbackResponse, MAIN_STEP_MESSAGE_ID, BaseActionStep
from utils.update import get_chat_id

ActionType = (ResponseTextMessage, CallbackResponse)
#FsmPipelineType = Optional[Type('FSMPipeline'), ActionType]


class PipelineActionType(IntEnum):
    NEXT = +1
    PREV = -1
    INFO = 0
    MOVE_TO = 2


class FSMPipeline(object):
    steps: List[Any]

    async def next(self, ctx: Any, bot: Bot, state: FSMContext, disable_information=False, *args, **kwargs):
        await self.__find_state_step(ctx, bot, state, PipelineActionType.NEXT, disable_information, *args, **kwargs)

    async def prev(self, ctx: Any, bot: Bot, state: FSMContext, disable_information=False, *args, **kwargs):
        await self.__find_state_step(ctx, bot, state, PipelineActionType.PREV, disable_information, *args, **kwargs)

    async def move_to(self, ctx: Any, bot: Bot, state: FSMContext, moved_state: State, disable_information=False, *args, **kwargs):
        await self.__find_state_step(ctx, bot, state, PipelineActionType.MOVE_TO, disable_information, founded_state=moved_state, *args, **kwargs)

    async def info(self, ctx: Any, bot: Bot, state: FSMContext, disable_information=False, **kwargs):
        await self.__find_state_step(ctx, bot, state, PipelineActionType.INFO, disable_information, **kwargs)

    async def __find_state_step(self, ctx: Any, bot: Bot, state: FSMContext, pipeline_method: PipelineActionType,
                                disable_information=False, founded_state: State = None, *args, **kwargs):
        founded_state: str = founded_state.state if founded_state else await state.get_state()
        steps_len = len(self.steps)

        for idx, step in enumerate(self.steps):
            if (isinstance(step, FSMPipeline) and self.__does_pipeline_contain_state(founded_state, step)) or \
                    (isinstance(step, ActionType) and step.state.state == founded_state):

                if pipeline_method == PipelineActionType.INFO:
                    current_pipeline = self.steps[idx]
                    await current_pipeline.information(ctx, bot=bot, state=state, *args, **kwargs)
                    return

                elif pipeline_method == PipelineActionType.MOVE_TO:
                    if isinstance(step, FSMPipeline):
                        step = step.steps[0]
                    await step.information(ctx, bot=bot, state=state, *args, **kwargs)
                    await state.set_state(step.state)
                    return

                elif pipeline_method == PipelineActionType.NEXT and idx == steps_len - 1:
                    raise Exception(f'The method {pipeline_method} cannot be executed in the last method of pipeline')
                elif pipeline_method == PipelineActionType.PREV and idx == 0:
                    raise Exception(f'The method {pipeline_method} cannot be executed in the first method of pipeline')

                for deep in range(1, 3):
                    deep *= pipeline_method.value
                    if steps_len > idx + deep >= 0:
                        found_pipeline = self.steps[idx + deep]

                        if isinstance(found_pipeline, FSMPipeline):
                            found_pipeline = found_pipeline.steps[0]

                        if found_pipeline.condition:
                            check = await found_pipeline.condition.call(ctx, state)
                            if not check:
                                continue

                        if not disable_information:
                            await found_pipeline.information(ctx, bot=bot, state=state, *args, **kwargs)

                        await state.set_state(found_pipeline.state)
                        return

        raise Exception(f'Handler for state: {founded_state} and method {pipeline_method.name} was not found')

    def __does_pipeline_contain_state(self, step_state: str, pipeline: FSMPipeline) -> bool:
        for step in pipeline.steps:
            if step.state.state == step_state:
                return True
        return False

    def set_pipeline(self, steps: []):
        self.steps = steps

    async def clean_main(self, ctx: Any, bot: Bot, state: FSMContext):
        data = await state.get_data()
        main_message_id = data.get(MAIN_STEP_MESSAGE_ID, None)
        if main_message_id:
            await bot.delete_message(get_chat_id(ctx), main_message_id)
        data[MAIN_STEP_MESSAGE_ID] = None
        await state.update_data(data)

    async def clean(self, ctx: Any, bot: Bot, state: FSMContext):
        data = await state.get_data()
        message_ids = data.get(MessageType.Utility, None)
        if message_ids:
            tasks = []
            for id in message_ids:
                tasks.append(bot.delete_message(get_chat_id(ctx), id))
            data[MessageType.Utility] = []
            await state.update_data(data)
            try:
                await asyncio.gather(*tasks)
            except:
                print("Error when deleting message")

    def build(self, router: Router):
        for idx, step in enumerate(self.steps):
            if isinstance(step, FSMPipeline):
                step.build(router)
            elif isinstance(step, BaseActionStep):

                if step.shipping_query_handler:
                    router.shipping_query.register(step.shipping_query_handler, *step.filters,
                                                   state=step.state)

                if step.pre_checkout_query_handler:
                    router.pre_checkout_query.register(step.pre_checkout_query_handler, state=step.state)

                if len(step.reply_navigation_handlers) > 0:
                    for reply_handler in step.reply_navigation_handlers:
                        router.message.register(reply_handler[1], text=reply_handler[0], state=step.state)

                if len(step.inline_navigation_handler) > 0:
                    for inline_handler in step.inline_navigation_handler:
                        router.callback_query.register(inline_handler[1], inline_handler[0], state=step.state)

                if isinstance(step, ResponseTextMessage):
                    router.message.register(step.handler, *step.filters, state=step.state)

                elif isinstance(step, CallbackResponse):
                    router.callback_query.register(step.handler, *step.filters,
                                                   state=step.state)