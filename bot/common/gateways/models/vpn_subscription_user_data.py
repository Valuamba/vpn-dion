import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionUserData")


@attr.s(auto_attribs=True)
class VpnSubscriptionUserData:
    """
    Attributes:
        user_id (int):
        pkid (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        update_at (Union[Unset, datetime.datetime]):
        user_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        is_bot_blocked (Union[Unset, bool]):
    """

    user_id: int
    pkid: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    update_at: Union[Unset, datetime.datetime] = UNSET
    user_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    is_bot_blocked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        pkid = self.pkid
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        update_at: Union[Unset, str] = UNSET
        if not isinstance(self.update_at, Unset):
            update_at = self.update_at.isoformat()

        user_name = self.user_name
        first_name = self.first_name
        last_name = self.last_name
        is_bot_blocked = self.is_bot_blocked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if update_at is not UNSET:
            field_dict["update_at"] = update_at
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_bot_blocked is not UNSET:
            field_dict["is_bot_blocked"] = is_bot_blocked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id")

        pkid = d.pop("pkid", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _update_at = d.pop("update_at", UNSET)
        update_at: Union[Unset, datetime.datetime]
        if isinstance(_update_at, Unset):
            update_at = UNSET
        else:
            update_at = isoparse(_update_at)

        user_name = d.pop("user_name", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_bot_blocked = d.pop("is_bot_blocked", UNSET)

        vpn_subscription_user_data = cls(
            user_id=user_id,
            pkid=pkid,
            created_at=created_at,
            update_at=update_at,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            is_bot_blocked=is_bot_blocked,
        )

        vpn_subscription_user_data.additional_properties = d
        return vpn_subscription_user_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
