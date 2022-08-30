from aiogram.fsm.state import StatesGroup, State


DEFAULT_MONTH_INDEX = 0
DEFAULT_DEVICE_INDEX = 0


class Fields:
    SelectedMonthDuration = "month_duration"
    SelectedSubscriptionOfferPkid = "selected_subscription_offer_pkid"
    SelectedSubscriptionOffer = "selected_subscription_offer"
    ConfiguredDeviceIndex = "configured_device_index"
    Devices = "devices"
    SubscriptionId = "subscription_id"


class DeviceFields:
    DeviceIndex = "index"
    SelectedCountryPk = "selected_country_pk"
    SelectedProtocolPk = "selected_protocol_pk"


class Device:
    def __init__(self, **kwargs):
        self.index = kwargs.get('index')
        self.selected_country_pk = kwargs.get('selected_country_pk', None)
        self.selected_protocol_pk = kwargs.get('selected_protocol_pk', None)


class ProcessSubscriptionStateGroup(StatesGroup):
    SelectTariff = State()
    SelectDevice = State()
    ConfigureDevice = State()
    ChooseProtocol = State()
    ChooseLocation = State()
    SelectPaymentMethod = State()


StateF = ProcessSubscriptionStateGroup

    