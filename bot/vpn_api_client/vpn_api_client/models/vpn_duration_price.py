from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnDurationPrice")


@attr.s(auto_attribs=True)
class VpnDurationPrice:
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

    def to_multipart(self) -> Dict[str, Any]:
        month_duration = (
            self.month_duration
            if isinstance(self.month_duration, Unset)
            else (None, str(self.month_duration).encode(), "text/plain")
        )
        currency = (
            self.currency if isinstance(self.currency, Unset) else (None, str(self.currency).encode(), "text/plain")
        )
        amount = self.amount if isinstance(self.amount, Unset) else (None, str(self.amount).encode(), "text/plain")
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
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

        vpn_duration_price = cls(
            month_duration=month_duration,
            currency=currency,
            amount=amount,
            pkid=pkid,
        )

        vpn_duration_price.additional_properties = d
        return vpn_duration_price

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
