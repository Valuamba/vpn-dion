import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.vpn_device_tariff_devices import VpnDeviceTariffDevices
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
        total_discount (str):
        initial_price (str):
        pkid (Union[Unset, int]):
        duration_data (Union[Unset, VpnDeviceTariffDurationData]):
        discount_percentage (Union[Unset, int]):
        discounted_price (Union[Unset, str]):
        devices (Union[Unset, VpnDeviceTariffDevices]):
    """

    duration: int
    devices_number: int
    operation: VpnDeviceTariffOperation
    total_discount: str
    initial_price: str
    pkid: Union[Unset, int] = UNSET
    duration_data: Union[Unset, VpnDeviceTariffDurationData] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    discounted_price: Union[Unset, str] = UNSET
    devices: Union[Unset, VpnDeviceTariffDevices] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration
        devices_number = self.devices_number
        operation = self.operation.value

        total_discount = self.total_discount
        initial_price = self.initial_price
        pkid = self.pkid
        duration_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration_data, Unset):
            duration_data = self.duration_data.to_dict()

        discount_percentage = self.discount_percentage
        discounted_price = self.discounted_price
        devices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "devices_number": devices_number,
                "operation": operation,
                "total_discount": total_discount,
                "initial_price": initial_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if duration_data is not UNSET:
            field_dict["duration_data"] = duration_data
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage
        if discounted_price is not UNSET:
            field_dict["discounted_price"] = discounted_price
        if devices is not UNSET:
            field_dict["devices"] = devices

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

        total_discount = (
            self.total_discount
            if isinstance(self.total_discount, Unset)
            else (None, str(self.total_discount).encode(), "text/plain")
        )
        initial_price = (
            self.initial_price
            if isinstance(self.initial_price, Unset)
            else (None, str(self.initial_price).encode(), "text/plain")
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
        discounted_price = (
            self.discounted_price
            if isinstance(self.discounted_price, Unset)
            else (None, str(self.discounted_price).encode(), "text/plain")
        )
        devices: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = (None, json.dumps(self.devices.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "duration": duration,
                "devices_number": devices_number,
                "operation": operation,
                "total_discount": total_discount,
                "initial_price": initial_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if duration_data is not UNSET:
            field_dict["duration_data"] = duration_data
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage
        if discounted_price is not UNSET:
            field_dict["discounted_price"] = discounted_price
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duration = d.pop("duration")

        devices_number = d.pop("devices_number")

        operation = VpnDeviceTariffOperation(d.pop("operation"))

        total_discount = d.pop("total_discount")

        initial_price = d.pop("initial_price")

        pkid = d.pop("pkid", UNSET)

        _duration_data = d.pop("duration_data", UNSET)
        duration_data: Union[Unset, VpnDeviceTariffDurationData]
        if isinstance(_duration_data, Unset):
            duration_data = UNSET
        else:
            duration_data = VpnDeviceTariffDurationData.from_dict(_duration_data)

        discount_percentage = d.pop("discount_percentage", UNSET)

        discounted_price = d.pop("discounted_price", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: Union[Unset, VpnDeviceTariffDevices]
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = VpnDeviceTariffDevices.from_dict(_devices)

        vpn_device_tariff = cls(
            duration=duration,
            devices_number=devices_number,
            operation=operation,
            total_discount=total_discount,
            initial_price=initial_price,
            pkid=pkid,
            duration_data=duration_data,
            discount_percentage=discount_percentage,
            discounted_price=discounted_price,
            devices=devices,
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
