from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionUserData")


@attr.s(auto_attribs=True)
class VpnSubscriptionUserData:
    """
    Attributes:
        user_id (int):
        user_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        is_bot_blocked (Union[Unset, bool]):
    """

    user_id: int
    user_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    is_bot_blocked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
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

        user_name = d.pop("user_name", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_bot_blocked = d.pop("is_bot_blocked", UNSET)

        vpn_subscription_user_data = cls(
            user_id=user_id,
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
