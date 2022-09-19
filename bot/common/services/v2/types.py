import json
from typing import Any, Dict, List, Type, TypeVar, Union, Optional
import attr


@attr.s(auto_attribs=True)
class VpnCountry:
    discount_percentage: int
    is_default: bool
    country: str
    pkid: int
    place: str
    locale_ru: str


@attr.s(auto_attribs=True)
class CreateSubscriptionDto:
    subscription_id: int
    freekassa_url: Optional[str]