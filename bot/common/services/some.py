import json
from typing import Any, Dict, List, Type, TypeVar, Union, Optional, Tuple

import pydantic
from pydantic import BaseModel,Field
from typing import List,Dict
from datetime import date
import attr


import json

# class Generic(BaseModel):
#     product: str
#     read
#     @classmethod
#     def from_dict(cls, dict):
#         obj = cls()
#         obj.__dict__.update(dict)
#         return obj
#
# data = '{"product": "name", "read_logs": {"log_type": "failure", "log_url": "123"}}'
#
# x = json.loads(data, object_hook=Generic.from_dict)
# print(x.product, x.read_logs.log_type, x.read_logs.log_url)


class FirstDto(BaseModel):
    user_id: int


# @attr.s(auto_attribs=True)
class VpnCountry(BaseModel):
    pkid: int
    country: str
    discount_percentage: str
    users: List[FirstDto]

data = '{"pkid" : 1, "country" : "3", "discount_percentage" : "Bangalore", "users": [{ "user_id": 12 }]}'
# data = '{"pkid" : 1, "country" : "3", "discount_percentage" : "Bangalore"}'

c = VpnCountry.parse_raw(data)

# students = pydantic.par(path='192.json', type_=classDTO.StudentsDTO)

parsed = json.loads(data)
user = parsed.pop('user')

country = VpnCountry(**parsed, user=FirstDto(**user))

s = json.loads(p1, object_hook=lambda d: FirstDto(**d))
x:VpnCountry = json.loads(data, object_hook=VpnCountry.from_dict)



print(x.pkid)