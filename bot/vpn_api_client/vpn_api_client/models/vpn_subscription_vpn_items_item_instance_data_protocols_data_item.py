from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_subscription_vpn_items_item_instance_data_protocols_data_item_protocol import (
    VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItemProtocol,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItem")


@attr.s(auto_attribs=True)
class VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItem:
    """
    Attributes:
        protocol (VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItemProtocol):
        pkid (Union[Unset, int]):
    """

    protocol: VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItemProtocol
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
        protocol = VpnSubscriptionVpnItemsItemInstanceDataProtocolsDataItemProtocol(d.pop("protocol"))

        pkid = d.pop("pkid", UNSET)

        vpn_subscription_vpn_items_item_instance_data_protocols_data_item = cls(
            protocol=protocol,
            pkid=pkid,
        )

        vpn_subscription_vpn_items_item_instance_data_protocols_data_item.additional_properties = d
        return vpn_subscription_vpn_items_item_instance_data_protocols_data_item

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
