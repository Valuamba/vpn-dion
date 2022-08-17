from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_subscription_vpn_items_item_protocol_data_protocol import (
    VpnSubscriptionVpnItemsItemProtocolDataProtocol,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionVpnItemsItemProtocolData")


@attr.s(auto_attribs=True)
class VpnSubscriptionVpnItemsItemProtocolData:
    """
    Attributes:
        protocol (VpnSubscriptionVpnItemsItemProtocolDataProtocol):
        pkid (Union[Unset, int]):
    """

    protocol: VpnSubscriptionVpnItemsItemProtocolDataProtocol
    pkid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol.value

        pkid = self.pkid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocol": protocol,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = VpnSubscriptionVpnItemsItemProtocolDataProtocol(d.pop("protocol"))

        pkid = d.pop("pkid", UNSET)

        vpn_subscription_vpn_items_item_protocol_data = cls(
            protocol=protocol,
            pkid=pkid,
        )

        vpn_subscription_vpn_items_item_protocol_data.additional_properties = d
        return vpn_subscription_vpn_items_item_protocol_data

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