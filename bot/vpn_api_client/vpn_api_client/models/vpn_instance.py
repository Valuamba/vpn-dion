import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.vpn_instance_country_data import VpnInstanceCountryData
from ..models.vpn_instance_protocols_data_item import VpnInstanceProtocolsDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnInstance")


@attr.s(auto_attribs=True)
class VpnInstance:
    """
    Attributes:
        ip_address (str):
        name (str):
        protocols (List[int]):
        protocols_data (List[VpnInstanceProtocolsDataItem]):
        is_online (bool):
        pkid (Union[Unset, int]):
        country (Union[Unset, None, int]):
        country_data (Union[Unset, VpnInstanceCountryData]):
    """

    ip_address: str
    name: str
    protocols: List[int]
    protocols_data: List[VpnInstanceProtocolsDataItem]
    is_online: bool
    pkid: Union[Unset, int] = UNSET
    country: Union[Unset, None, int] = UNSET
    country_data: Union[Unset, VpnInstanceCountryData] = UNSET
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

    def to_multipart(self) -> Dict[str, Any]:
        ip_address = (
            self.ip_address
            if isinstance(self.ip_address, Unset)
            else (None, str(self.ip_address).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        _temp_protocols = self.protocols
        protocols = (None, json.dumps(_temp_protocols).encode(), "application/json")

        _temp_protocols_data = []
        for protocols_data_item_data in self.protocols_data:
            protocols_data_item = protocols_data_item_data.to_dict()

            _temp_protocols_data.append(protocols_data_item)
        protocols_data = (None, json.dumps(_temp_protocols_data).encode(), "application/json")

        is_online = (
            self.is_online if isinstance(self.is_online, Unset) else (None, str(self.is_online).encode(), "text/plain")
        )
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")
        country = self.country if isinstance(self.country, Unset) else (None, str(self.country).encode(), "text/plain")
        country_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.country_data, Unset):
            country_data = (None, json.dumps(self.country_data.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
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
            protocols_data_item = VpnInstanceProtocolsDataItem.from_dict(protocols_data_item_data)

            protocols_data.append(protocols_data_item)

        is_online = d.pop("is_online")

        pkid = d.pop("pkid", UNSET)

        country = d.pop("country", UNSET)

        _country_data = d.pop("country_data", UNSET)
        country_data: Union[Unset, VpnInstanceCountryData]
        if isinstance(_country_data, Unset):
            country_data = UNSET
        else:
            country_data = VpnInstanceCountryData.from_dict(_country_data)

        vpn_instance = cls(
            ip_address=ip_address,
            name=name,
            protocols=protocols,
            protocols_data=protocols_data,
            is_online=is_online,
            pkid=pkid,
            country=country,
            country_data=country_data,
        )

        vpn_instance.additional_properties = d
        return vpn_instance

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
