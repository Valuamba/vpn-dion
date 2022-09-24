from aiogram.fsm.state import StatesGroup, State


class ReviewsStateGroup(StatesGroup):
    SeeReviews = State()


class Fields:
   pass


StateF = ReviewsStateGroup