import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr


@attr.s(auto_attribs=True)
class VpnCountry:
    pkid: int
    country: str
    discount_percentage: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

data = '{"pkid" : 1, "country" : "3", "discount_percentage" : "Bangalore"}'
x:VpnCountry = json.loads(data, object_hook=lambda d: VpnCountry(**d))



print(x.pkid)