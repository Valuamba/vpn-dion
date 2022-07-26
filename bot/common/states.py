from aiogram.dispatcher.fsm.state import StatesGroup, State


class CommandStates(StatesGroup):
    MAIN = State()
