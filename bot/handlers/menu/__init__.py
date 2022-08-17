from aiogram.fsm.state import StatesGroup, State


class MenuStatesGroup(StatesGroup):
    Menu = State()
    Help = State()
    AvailableLocations = State()
    About = State()


StateF = MenuStatesGroup