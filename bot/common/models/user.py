from enum import Enum

from pydantic import Field

from common.models.base import TimeBaseModel


class UserRoles(str, Enum):
    new = 'new'
    user = 'user'
    admin = 'admin'
    manager = 'manager'
    blocked = 'blocked'


class UserModel(TimeBaseModel):
    id: int = Field(...)
    language: str = 'en'
    real_language: str = 'en'
    role: UserRoles = Field(default=UserRoles.new)
    status: str = 'member'
    nikname: str = Field(default=None)
    full_name: str = Field(default=None)
    off_name: str = Field(default=None)
    phonenumber: str = Field(default=None)
    isAuthorized: bool = Field(default=False)
    isAcceptedTermsOfUse: bool = Field(default=False)
    is_bot_blocked: bool = Field(default=False)
    is_blocked: bool = Field(default=False)
    balance: int = Field(default=0)

    class Collection:
        name = "UserModel"
