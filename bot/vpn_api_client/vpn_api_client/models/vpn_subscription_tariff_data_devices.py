from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VpnSubscriptionTariffDataDevices")


@attr.s(auto_attribs=True)
class VpnSubscriptionTariffDataDevices:
    """
    Attributes:
        country_id (int):
        protocol_id (int):
    """

    country_id: int
    protocol_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country_id = self.country_id
        protocol_id = self.protocol_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_id": country_id,
                "protocol_id": protocol_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_id = d.pop("country_id")

        protocol_id = d.pop("protocol_id")

        vpn_subscription_tariff_data_devices = cls(
            country_id=country_id,
            protocol_id=protocol_id,
        )

        vpn_subscription_tariff_data_devices.additional_properties = d
        return vpn_subscription_tariff_data_devices

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
