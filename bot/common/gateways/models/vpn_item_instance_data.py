from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.vpn_item_instance_data_country_data import VpnItemInstanceDataCountryData
from ..models.vpn_item_instance_data_protocols_data_item import VpnItemInstanceDataProtocolsDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnItemInstanceData")


@attr.s(auto_attribs=True)
class VpnItemInstanceData:
    """
    Attributes:
        ip_address (str):
        name (str):
        protocols (List[int]):
        protocols_data (List[VpnItemInstanceDataProtocolsDataItem]):
        is_online (bool):
        pkid (Union[Unset, int]):
        country (Union[Unset, None, int]):
        country_data (Union[Unset, VpnItemInstanceDataCountryData]):
    """

    ip_address: str
    name: str
    protocols: List[int]
    protocols_data: List[VpnItemInstanceDataProtocolsDataItem]
    is_online: bool
    pkid: Union[Unset, int] = UNSET
    country: Union[Unset, None, int] = UNSET
    country_data: Union[Unset, VpnItemInstanceDataCountryData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip_address = self.ip_address
        name = self.name
        protocols = self.protocols

        protocols_data = []
        for protocols_data_item_data in self.protocols_data:
            protocols_data_item = protocols_data_item_data.to_dict()

            protocols_data.append(protocols_data_item)

        is_online = self.is_online
        pkid = self.pkid
        country = self.country
        country_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country_data, Unset):
            country_data = self.country_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address": ip_address,
                "name": name,
                "protocols": protocols,
                "protocols_data": protocols_data,
                "is_online": is_online,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if country is not UNSET:
            field_dict["country"] = country
        if country_data is not UNSET:
            field_dict["country_data"] = country_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address = d.pop("ip_address")

        name = d.pop("name")

        protocols = cast(List[int], d.pop("protocols"))

        protocols_data = []
        _protocols_data = d.pop("protocols_data")
        for protocols_data_item_data in _protocols_data:
            protocols_data_item = VpnItemInstanceDataProtocolsDataItem.from_dict(protocols_data_item_data)

            protocols_data.append(protocols_data_item)

        is_online = d.pop("is_online")

        pkid = d.pop("pkid", UNSET)

        country = d.pop("country", UNSET)

        _country_data = d.pop("country_data", UNSET)
        country_data: Union[Unset, VpnItemInstanceDataCountryData]
        if isinstance(_country_data, Unset):
            country_data = UNSET
        else:
            country_data = VpnItemInstanceDataCountryData.from_dict(_country_data)

        vpn_item_instance_data = cls(
            ip_address=ip_address,
            name=name,
            protocols=protocols,
            protocols_data=protocols_data,
            is_online=is_online,
            pkid=pkid,
            country=country,
            country_data=country_data,
        )

        vpn_item_instance_data.additional_properties = d
        return vpn_item_instance_data

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
