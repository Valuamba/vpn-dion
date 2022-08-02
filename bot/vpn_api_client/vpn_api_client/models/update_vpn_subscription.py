from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.update_vpn_subscription_status import UpdateVpnSubscriptionStatus

T = TypeVar("T", bound="UpdateVpnSubscription")


@attr.s(auto_attribs=True)
class UpdateVpnSubscription:
    """
    Attributes:
        status (UpdateVpnSubscriptionStatus):
    """

    status: UpdateVpnSubscriptionStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        status = (None, str(self.status.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = UpdateVpnSubscriptionStatus(d.pop("status"))

        update_vpn_subscription = cls(
            status=status,
        )

        update_vpn_subscription.additional_properties = d
        return update_vpn_subscription

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
