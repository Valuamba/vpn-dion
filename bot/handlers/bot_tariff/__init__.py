from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import State, StatesGroup


class Fields:
    SelectedTariffId = "selectedTariffId"
    SelectedCountryId = "selectedCountryId"
    CreatedSubscription = "createdSubscriptionId"
    FreekassaUrl = "freekassaUrl"


class BotTariffGroup(StatesGroup):
    SelectCountry = State()
    SelectPaymentMethod = State()


class VpnPreCheckoutCD(CallbackData, prefix="vpn-sub-precheckout"):
    subscription_id: int


StateF = BotTariffGroup