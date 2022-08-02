from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.vpn_country_place import VpnCountryPlace
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnCountry")


@attr.s(auto_attribs=True)
class VpnCountry:
    """
    Attributes:
        pkid (Union[Unset, int]):
        place (Union[Unset, VpnCountryPlace]):
        discount_percentage (Union[Unset, int]):
    """

    pkid: Union[Unset, int] = UNSET
    place: Union[Unset, VpnCountryPlace] = UNSET
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

    def to_multipart(self) -> Dict[str, Any]:
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")
        place: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.place, Unset):
            place = (None, str(self.place.value).encode(), "text/plain")

        discount_percentage = (
            self.discount_percentage
            if isinstance(self.discount_percentage, Unset)
            else (None, str(self.discount_percentage).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
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
        place: Union[Unset, VpnCountryPlace]
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = VpnCountryPlace(_place)

        discount_percentage = d.pop("discount_percentage", UNSET)

        vpn_country = cls(
            pkid=pkid,
            place=place,
            discount_percentage=discount_percentage,
        )

        vpn_country.additional_properties = d
        return vpn_country

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
