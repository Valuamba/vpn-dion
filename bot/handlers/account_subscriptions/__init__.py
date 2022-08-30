from aiogram.fsm.state import StatesGroup, State


class AccountSubscriptionsStateGroup(StatesGroup):
    AllUserSubscriptions = State()
    UserSubscriptionDevices = State()
    UserDeviceSubDetails = State()


class Fields:
    SubscriptionId = "subscription_id"
    VpnDeviceId = "vpn_device_id"


StateF = AccountSubscriptionsStateGroup