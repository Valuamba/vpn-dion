from aiogram.fsm.state import StatesGroup, State


class FeedbackStateGroup(StatesGroup):
    WriteFeedBackMessage = State()
    SuccessSendingHelp = State()


StateF = FeedbackStateGroup