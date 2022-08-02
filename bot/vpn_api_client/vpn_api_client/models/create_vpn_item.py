from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateVpnItem")


@attr.s(auto_attribs=True)
class CreateVpnItem:
    """
    Attributes:
        protocol (int):
        pkid (Union[Unset, int]):
        instance (Union[Unset, None, int]):
        vpn_subscription (Union[Unset, None, int]):
    """

    protocol: int
    pkid: Union[Unset, int] = UNSET
    instance: Union[Unset, None, int] = UNSET
    vpn_subscription: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol
        pkid = self.pkid
        instance = self.instance
        vpn_subscription = self.vpn_subscription

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
        if vpn_subscription is not UNSET:
            field_dict["vpn_subscription"] = vpn_subscription

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        protocol = (
            self.protocol if isinstance(self.protocol, Unset) else (None, str(self.protocol).encode(), "text/plain")
        )
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")
        instance = (
            self.instance if isinstance(self.instance, Unset) else (None, str(self.instance).encode(), "text/plain")
        )
        vpn_subscription = (
            self.vpn_subscription
            if isinstance(self.vpn_subscription, Unset)
            else (None, str(self.vpn_subscription).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "protocol": protocol,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if instance is not UNSET:
            field_dict["instance"] = instance
        if vpn_subscription is not UNSET:
            field_dict["vpn_subscription"] = vpn_subscription

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = d.pop("protocol")

        pkid = d.pop("pkid", UNSET)

        instance = d.pop("instance", UNSET)

        vpn_subscription = d.pop("vpn_subscription", UNSET)

        create_vpn_item = cls(
            protocol=protocol,
            pkid=pkid,
            instance=instance,
            vpn_subscription=vpn_subscription,
        )

        create_vpn_item.additional_properties = d
        return create_vpn_item

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
