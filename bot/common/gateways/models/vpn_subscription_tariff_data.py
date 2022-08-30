from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_subscription_tariff_data_duration_data import VpnSubscriptionTariffDataDurationData
from ..models.vpn_subscription_tariff_data_operation import VpnSubscriptionTariffDataOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionTariffData")


@attr.s(auto_attribs=True)
class VpnSubscriptionTariffData:
    """
    Attributes:
        duration (int):
        devices_number (int):
        operation (VpnSubscriptionTariffDataOperation):
        result_price (str):
        pkid (Union[Unset, int]):
        duration_data (Union[Unset, VpnSubscriptionTariffDataDurationData]):
        discount_percentage (Union[Unset, int]):
    """

    duration: int
    devices_number: int
    operation: VpnSubscriptionTariffDataOperation
    result_price: str
    pkid: Union[Unset, int] = UNSET
    duration_data: Union[Unset, VpnSubscriptionTariffDataDurationData] = UNSET
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

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duration = d.pop("duration")

        devices_number = d.pop("devices_number")

        operation = VpnSubscriptionTariffDataOperation(d.pop("operation"))

        result_price = d.pop("result_price")

        pkid = d.pop("pkid", UNSET)

        _duration_data = d.pop("duration_data", UNSET)
        duration_data: Union[Unset, VpnSubscriptionTariffDataDurationData]
        if isinstance(_duration_data, Unset):
            duration_data = UNSET
        else:
            duration_data = VpnSubscriptionTariffDataDurationData.from_dict(_duration_data)

        discount_percentage = d.pop("discount_percentage", UNSET)

        vpn_subscription_tariff_data = cls(
            duration=duration,
            devices_number=devices_number,
            operation=operation,
            result_price=result_price,
            pkid=pkid,
            duration_data=duration_data,
            discount_percentage=discount_percentage,
        )

        vpn_subscription_tariff_data.additional_properties = d
        return vpn_subscription_tariff_data

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
