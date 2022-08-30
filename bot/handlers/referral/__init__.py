from aiogram.fsm.state import StatesGroup, State


class ReferralStateGroup(StatesGroup):
    ReferralMenu = State()
    AcceptGettingReward = State()
    ActivatedFreeSubInfo = State()


class Fields:
    ActivatedMonthCount = "activatedMonthCount"
    ActivatedSubscriptionId = "activatedSubscriptionId"


StateF = ReferralStateGroup