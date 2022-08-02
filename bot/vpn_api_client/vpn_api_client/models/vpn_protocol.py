from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_protocol_protocol import VpnProtocolProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnProtocol")


@attr.s(auto_attribs=True)
class VpnProtocol:
    """
    Attributes:
        protocol (VpnProtocolProtocol):
        pkid (Union[Unset, int]):
    """

    protocol: VpnProtocolProtocol
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

    def to_multipart(self) -> Dict[str, Any]:
        protocol = (None, str(self.protocol.value).encode(), "text/plain")

        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = VpnProtocolProtocol(d.pop("protocol"))

        pkid = d.pop("pkid", UNSET)

        vpn_protocol = cls(
            protocol=protocol,
            pkid=pkid,
        )

        vpn_protocol.additional_properties = d
        return vpn_protocol

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
