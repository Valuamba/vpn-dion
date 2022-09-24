import decimal
import json
from datetime import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, Optional
import attr
from pydantic import BaseModel


class VpnCountry(BaseModel):
    discount_percentage: Optional[int]
    is_default: Optional[bool]
    country: str
    pkid: int
    place: str
    locale_ru: str


class VpnCountryList(BaseModel):
    __root__: List[VpnCountry]


@attr.s(auto_attribs=True)
class CreateSubscriptionDto:
    subscription_id: int
    freekassa_url: Optional[str]


class UserDto(BaseModel):
    user_id: int


class ProtocolDto(BaseModel):
    pkid: int


class VpnItemDto(BaseModel):
    country_data: VpnCountry
    protocol_data: ProtocolDto


class SubscriptionDetailsDto(BaseModel):
    pkid: int
    month_duration: Optional[int]
    days_duration: Optional[int]
    devices_number: int
    status: str
    is_referral: bool
    price: decimal.Decimal
    discount: int
    subscription_end: Optional[datetime]
    reminder_state: int

    user_data: UserDto
    vpn_items_list: List[VpnItemDto]


class VpnDurationTariff(BaseModel):
    month_duration: int


class VpnDeviceTariff(BaseModel):
    pkid: int
    total_discount: int
    price: int
    duration_data: VpnDurationTariff


class VpnDeviceTariffList(BaseModel):
    __root__: List[VpnDeviceTariff]


