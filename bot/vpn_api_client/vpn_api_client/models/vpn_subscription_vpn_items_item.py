from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_subscription_vpn_items_item_instance_data import VpnSubscriptionVpnItemsItemInstanceData
from ..models.vpn_subscription_vpn_items_item_protocol_data import VpnSubscriptionVpnItemsItemProtocolData
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionVpnItemsItem")


@attr.s(auto_attribs=True)
class VpnSubscriptionVpnItemsItem:
    """
    Attributes:
        protocol (int):
        public_key (str):
        private_key (str):
        address (str):
        dns (str):
        preshared_key (str):
        endpoint (str):
        allowed_ips (str):
        config_name (str):
        pkid (Union[Unset, int]):
        instance (Union[Unset, None, int]):
        instance_data (Union[Unset, VpnSubscriptionVpnItemsItemInstanceData]):
        protocol_data (Union[Unset, VpnSubscriptionVpnItemsItemProtocolData]):
    """

    protocol: int
    public_key: str
    private_key: str
    address: str
    dns: str
    preshared_key: str
    endpoint: str
    allowed_ips: str
    config_name: str
    pkid: Union[Unset, int] = UNSET
    instance: Union[Unset, None, int] = UNSET
    instance_data: Union[Unset, VpnSubscriptionVpnItemsItemInstanceData] = UNSET
    protocol_data: Union[Unset, VpnSubscriptionVpnItemsItemProtocolData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol
        public_key = self.public_key
        private_key = self.private_key
        address = self.address
        dns = self.dns
        preshared_key = self.preshared_key
        endpoint = self.endpoint
        allowed_ips = self.allowed_ips
        config_name = self.config_name
        pkid = self.pkid
        instance = self.instance
        instance_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instance_data, Unset):
            instance_data = self.instance_data.to_dict()

        protocol_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.protocol_data, Unset):
            protocol_data = self.protocol_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocol": protocol,
                "public_key": public_key,
                "private_key": private_key,
                "address": address,
                "dns": dns,
                "preshared_key": preshared_key,
                "endpoint": endpoint,
                "allowed_ips": allowed_ips,
                "config_name": config_name,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if instance is not UNSET:
            field_dict["instance"] = instance
        if instance_data is not UNSET:
            field_dict["instance_data"] = instance_data
        if protocol_data is not UNSET:
            field_dict["protocol_data"] = protocol_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = d.pop("protocol")

        public_key = d.pop("public_key")

        private_key = d.pop("private_key")

        address = d.pop("address")

        dns = d.pop("dns")

        preshared_key = d.pop("preshared_key")

        endpoint = d.pop("endpoint")

        allowed_ips = d.pop("allowed_ips")

        config_name = d.pop("config_name")

        pkid = d.pop("pkid", UNSET)

        instance = d.pop("instance", UNSET)

        _instance_data = d.pop("instance_data", UNSET)
        instance_data: Union[Unset, VpnSubscriptionVpnItemsItemInstanceData]
        if isinstance(_instance_data, Unset):
            instance_data = UNSET
        else:
            instance_data = VpnSubscriptionVpnItemsItemInstanceData.from_dict(_instance_data)

        _protocol_data = d.pop("protocol_data", UNSET)
        protocol_data: Union[Unset, VpnSubscriptionVpnItemsItemProtocolData]
        if isinstance(_protocol_data, Unset):
            protocol_data = UNSET
        else:
            protocol_data = VpnSubscriptionVpnItemsItemProtocolData.from_dict(_protocol_data)

        vpn_subscription_vpn_items_item = cls(
            protocol=protocol,
            public_key=public_key,
            private_key=private_key,
            address=address,
            dns=dns,
            preshared_key=preshared_key,
            endpoint=endpoint,
            allowed_ips=allowed_ips,
            config_name=config_name,
            pkid=pkid,
            instance=instance,
            instance_data=instance_data,
            protocol_data=protocol_data,
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
