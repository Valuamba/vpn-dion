from enum import IntEnum
from typing import List


class SubscriptionOfferDevicesType(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR_OR_MORE = 4


class SubscriptionOffer:
    def __init__(self, **kwargs):
        self.pkid = kwargs.get('pkid')
        self.month_duration = kwargs.get('month_duration')
        self.devices_count = kwargs.get('devices_count')
        self.discount_percentage = kwargs.get('discount_percentage')


class SubscriptionDurationOffer:
    def __init__(self, **kwargs):
        self.pkid: int = kwargs.get('pkid')
        self.month_duration: int = kwargs.get('month_duration')
        self.device_offers: List[SubscriptionDeviceOffer] = kwargs.get('device_offers')


class SubscriptionDeviceOffer:
    def __init__(self, **kwargs):
        self.pkid: int = kwargs.get('pkid')
        self.device_type: SubscriptionOfferDevicesType = kwargs.get('device_type')
        self.discount_percentage: float = kwargs.get('discount_percentage')


class CountryOffer:
    country: str
    discount_percentage: float