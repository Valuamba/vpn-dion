from aiogram.fsm.state import StatesGroup, State


class MenuStatesGroup(StatesGroup):
    Menu = State()


StateF = MenuStatesGroup