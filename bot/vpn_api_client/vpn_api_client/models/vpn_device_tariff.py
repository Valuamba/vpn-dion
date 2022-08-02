import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.vpn_device_tariff_duration_data import VpnDeviceTariffDurationData
from ..models.vpn_device_tariff_operation import VpnDeviceTariffOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnDeviceTariff")


@attr.s(auto_attribs=True)
class VpnDeviceTariff:
    """
    Attributes:
        duration (int):
        devices_number (int):
        operation (VpnDeviceTariffOperation):
        result_price (str):
        pkid (Union[Unset, int]):
        duration_data (Union[Unset, VpnDeviceTariffDurationData]):
        discount_percentage (Union[Unset, int]):
    """

    duration: int
    devices_number: int
    operation: VpnDeviceTariffOperation
    result_price: str
    pkid: Union[Unset, int] = UNSET
    duration_data: Union[Unset, VpnDeviceTariffDurationData] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration
        devices_number = self.devices_number
        operation = self.operation.value

        result_price = self.result_price
        pkid = self.pkid
        duration_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration_data, Unset):
            duration_data = self.duration_data.to_dict()

        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "devices_number": devices_number,
                "operation": operation,
                "result_price": result_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if duration_data is not UNSET:
            field_dict["duration_data"] = duration_data
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        duration = (
            self.duration if isinstance(self.duration, Unset) else (None, str(self.duration).encode(), "text/plain")
        )
        devices_number = (
            self.devices_number
            if isinstance(self.devices_number, Unset)
            else (None, str(self.devices_number).encode(), "text/plain")
        )
        operation = (None, str(self.operation.value).encode(), "text/plain")

        result_price = (
            self.result_price
            if isinstance(self.result_price, Unset)
            else (None, str(self.result_price).encode(), "text/plain")
        )
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")
        duration_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.duration_data, Unset):
            duration_data = (None, json.dumps(self.duration_data.to_dict()).encode(), "application/json")

        discount_percentage = (
            self.discount_percentage
            if isinstance(self.discount_percentage, Unset)
            else (None, str(self.discount_percentage).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "duration": duration,
                "devices_number": devices_number,
                "operation": operation,
                "result_price": result_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if duration_data is not UNSET:
            field_dict["duration_data"] = duration_data
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duration = d.pop("duration")

        devices_number = d.pop("devices_number")

        operation = VpnDeviceTariffOperation(d.pop("operation"))

        result_price = d.pop("result_price")

        pkid = d.pop("pkid", UNSET)

        _duration_data = d.pop("duration_data", UNSET)
        duration_data: Union[Unset, VpnDeviceTariffDurationData]
        if isinstance(_duration_data, Unset):
            duration_data = UNSET
        else:
            duration_data = VpnDeviceTariffDurationData.from_dict(_duration_data)

        discount_percentage = d.pop("discount_percentage", UNSET)

        vpn_device_tariff = cls(
            duration=duration,
            devices_number=devices_number,
            operation=operation,
            result_price=result_price,
            pkid=pkid,
            duration_data=duration_data,
            discount_percentage=discount_percentage,
        )

        vpn_device_tariff.additional_properties = d
        return vpn_device_tariff

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
