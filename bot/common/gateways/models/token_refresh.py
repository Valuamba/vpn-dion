from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenRefresh")


@attr.s(auto_attribs=True)
class TokenRefresh:
    """
    Attributes:
        refresh (str):
        access (Union[Unset, str]):
    """

    refresh: str
    access: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refresh = self.refresh
        access = self.access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refresh": refresh,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        refresh = self.refresh if isinstance(self.refresh, Unset) else (None, str(self.refresh).encode(), "text/plain")
        access = self.access if isinstance(self.access, Unset) else (None, str(self.access).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "refresh": refresh,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refresh = d.pop("refresh")

        access = d.pop("access", UNSET)

        token_refresh = cls(
            refresh=refresh,
            access=access,
        )

        token_refresh.additional_properties = d
        return token_refresh

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
