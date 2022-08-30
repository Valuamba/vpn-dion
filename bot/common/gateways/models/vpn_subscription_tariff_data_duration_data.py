from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionTariffDataDurationData")


@attr.s(auto_attribs=True)
class VpnSubscriptionTariffDataDurationData:
    """
    Attributes:
        month_duration (int):
        currency (str):
        amount (str):
        pkid (Union[Unset, int]):
    """

    month_duration: int
    currency: str
    amount: str
    pkid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        month_duration = self.month_duration
        currency = self.currency
        amount = self.amount
        pkid = self.pkid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month_duration": month_duration,
                "currency": currency,
                "amount": amount,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        month_duration = d.pop("month_duration")

        currency = d.pop("currency")

        amount = d.pop("amount")

        pkid = d.pop("pkid", UNSET)

        vpn_subscription_tariff_data_duration_data = cls(
            month_duration=month_duration,
            currency=currency,
            amount=amount,
            pkid=pkid,
        )

        vpn_subscription_tariff_data_duration_data.additional_properties = d
        return vpn_subscription_tariff_data_duration_data

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
