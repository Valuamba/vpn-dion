from aiogram.dispatcher.fsm.state import StatesGroup, State


class MenuStatesGroup(StatesGroup):
    Menu = State()


StateF = MenuStatesGroup