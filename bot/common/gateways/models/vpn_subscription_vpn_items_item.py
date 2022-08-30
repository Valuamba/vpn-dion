from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionVpnItemsItem")


@attr.s(auto_attribs=True)
class VpnSubscriptionVpnItemsItem:
    """
    Attributes:
        protocol (int):
        pkid (Union[Unset, int]):
        instance (Union[Unset, None, int]):
    """

    protocol: int
    pkid: Union[Unset, int] = UNSET
    instance: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol
        pkid = self.pkid
        instance = self.instance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocol": protocol,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = d.pop("protocol")

        pkid = d.pop("pkid", UNSET)

        instance = d.pop("instance", UNSET)

        vpn_subscription_vpn_items_item = cls(
            protocol=protocol,
            pkid=pkid,
            instance=instance,
        )

        vpn_subscription_vpn_items_item.additional_properties = d
        return vpn_subscription_vpn_items_item

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
