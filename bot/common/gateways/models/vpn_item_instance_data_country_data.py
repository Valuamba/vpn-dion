from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.vpn_item_instance_data_country_data_place import VpnItemInstanceDataCountryDataPlace
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnItemInstanceDataCountryData")


@attr.s(auto_attribs=True)
class VpnItemInstanceDataCountryData:
    """
    Attributes:
        pkid (Union[Unset, int]):
        place (Union[Unset, VpnItemInstanceDataCountryDataPlace]):
        discount_percentage (Union[Unset, int]):
    """

    pkid: Union[Unset, int] = UNSET
    place: Union[Unset, VpnItemInstanceDataCountryDataPlace] = UNSET
    discount_percentage: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pkid = self.pkid
        place: Union[Unset, str] = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.value

        discount_percentage = self.discount_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if place is not UNSET:
            field_dict["place"] = place
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pkid = d.pop("pkid", UNSET)

        _place = d.pop("place", UNSET)
        place: Union[Unset, VpnItemInstanceDataCountryDataPlace]
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = VpnItemInstanceDataCountryDataPlace(_place)

        discount_percentage = d.pop("discount_percentage", UNSET)

        vpn_item_instance_data_country_data = cls(
            pkid=pkid,
            place=place,
            discount_percentage=discount_percentage,
        )

        vpn_item_instance_data_country_data.additional_properties = d
        return vpn_item_instance_data_country_data

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
