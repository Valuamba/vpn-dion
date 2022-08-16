from abc import ABC
from typing import Union, Any, List, Tuple, Generic, TypeVar
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.dispatcher.event.handler import CallbackType
from aiogram.filters import ContentTypesFilter
from aiogram.fsm.state import StatesGroup, State

UTILITY_MESSAGE_IDS = "utility_message_ids"
MAIN_STEP_MESSAGE_ID = "main_step_message_id"

ReplyNavigationType = Tuple[str, CallbackType]
InlineNavigationType = Tuple[CallbackType, CallbackType]


class BaseActionStep(ABC):
    def __init__(self,
                 state: State,
                 handler: CallbackType,
                 information: CallbackType,
                 condition: any = None,
                 filters: List[CallbackType] = None,
                 reply_navigation_handlers: List[ReplyNavigationType] = None,
                 inline_navigation_handler: List[InlineNavigationType] = None,
                 shipping_query_handler: CallbackType = None,
                 pre_checkout_query_handler: CallbackType = None):

        if filters is None:
            filters = []

        if reply_navigation_handlers is None:
            reply_navigation_handlers = []

        if inline_navigation_handler is None:
            inline_navigation_handler = []

        if condition is not None:
            self.condition = CallbackType(condition)

        self.state = state
        self.handler = handler
        self.information = information
        self.condition = condition
        self.filters = filters
        self.reply_navigation_handlers = reply_navigation_handlers
        self.inline_navigation_handler = inline_navigation_handler
        self.shipping_query_handler = shipping_query_handler
        self.pre_checkout_query_handler = pre_checkout_query_handler


class MessageStep(BaseActionStep):
    @property
    def content_types(self) -> [str]:
        raise NotImplementedError

    def __init__(self, **kwargs):
        super(MessageStep, self).__init__(**kwargs)
        self.filters.append(ContentTypesFilter(content_types=self.content_types))


class ResponseTextMessage(MessageStep):
    content_types = [types.ContentType.TEXT]
    
    def __init__(self, content_types: [str] = None, **kwargs):
        if content_types:
            self.content_types = content_types
        super(ResponseTextMessage, self).__init__(**kwargs)


# T = TypeVar("T")


class CallbackResponse(BaseActionStep):
    def __init__(self, cq_filter: CallbackType = None, **kwargs):
        super(CallbackResponse, self).__init__(**kwargs)
        if cq_filter:
            self.filters.append(cq_filter)


class InformationalStep(BaseActionStep):
    def __init__(self, **kwargs):
        super(InformationalStep, self).__init__(**kwargs)