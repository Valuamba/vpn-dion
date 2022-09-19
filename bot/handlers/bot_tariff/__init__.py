from aiogram.fsm.state import State, StatesGroup


class Fields:
    SelectedTariffId = "selectedTariffId"
    SelectedCountryId = "selectedCountryId"
    CreatedSubscription = "createdSubscriptionId"
    FreekassaUrl = "freekassaUrl"


class BotTariffGroup(StatesGroup):
    SelectCountry = State()
    SelectPaymentMethod = State()


StateF = BotTariffGroup