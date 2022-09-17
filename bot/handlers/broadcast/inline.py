from aiogram.filters.callback_data import CallbackData

from common.keyboard.utility_keyboards import NavCD, NavType
from utils.markup_constructor import InlineMarkupConstructor


class CancelCD(CallbackData, prefix='cancel'):
    pass


class CancelKb(InlineMarkupConstructor):

    def get(self):
        schema = [1]
        actions = [
            {'text': 'Отмена', 'callback_data': NavCD(type=NavType.BACK).pack()},
        ]
        return self.markup(actions, schema)
