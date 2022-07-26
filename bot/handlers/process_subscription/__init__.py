from aiogram.dispatcher.fsm.state import StatesGroup, State


DEFAULT_MONTH_INDEX = 0
DEFAULT_DEVICE_INDEX = 0


class Fields:
    SelectedMonth = "selected_month_tariff"
    SelectedDevice = "selected_device_tariff"


class ProcessSubscriptionStateGroup(StatesGroup):
    SelectTariff = State()
    ChooseProtocol = State()
    ChooseLocation = State()


StateF = ProcessSubscriptionStateGroup

    