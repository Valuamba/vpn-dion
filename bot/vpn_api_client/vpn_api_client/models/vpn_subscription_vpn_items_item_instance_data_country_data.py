from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscriptionVpnItemsItemInstanceDataCountryData")


@attr.s(auto_attribs=True)
class VpnSubscriptionVpnItemsItemInstanceDataCountryData:
    """
    Attributes:
        pkid (Union[Unset, int]):
        country (Union[Unset, str]):
        discount_percentage (Union[Unset, int]):
    """

    pkid: Union[Unset, int] = UNSET
    country: Union[Unset, str] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pkid = self.pkid
        country = self.country
        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if country is not UNSET:
            field_dict["country"] = country
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pkid = d.pop("pkid", UNSET)

        country = d.pop("country", UNSET)

        discount_percentage = d.pop("discount_percentage", UNSET)

        vpn_subscription_vpn_items_item_instance_data_country_data = cls(
            pkid=pkid,
            country=country,
            discount_percentage=discount_percentage,
        )

        vpn_subscription_vpn_items_item_instance_data_country_data.additional_properties = d
        return vpn_subscription_vpn_items_item_instance_data_country_data

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
