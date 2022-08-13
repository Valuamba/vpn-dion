import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.vpn_subscription_status import VpnSubscriptionStatus
from ..models.vpn_subscription_tariff_data import VpnSubscriptionTariffData
from ..models.vpn_subscription_user_data import VpnSubscriptionUserData
from ..models.vpn_subscription_vpn_items_item import VpnSubscriptionVpnItemsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnSubscription")


@attr.s(auto_attribs=True)
class VpnSubscription:
    """
    Attributes:
        user (str):
        discount (str):
        status (VpnSubscriptionStatus):
        discounted_price (str):
        pkid (Union[Unset, int]):
        user_data (Union[Unset, VpnSubscriptionUserData]):
        tariff (Union[Unset, None, int]):
        tariff_data (Union[Unset, VpnSubscriptionTariffData]):
        vpn_items (Union[Unset, List[VpnSubscriptionVpnItemsItem]]):
    """

    user: str
    discount: str
    status: VpnSubscriptionStatus
    discounted_price: str
    pkid: Union[Unset, int] = UNSET
    user_data: Union[Unset, VpnSubscriptionUserData] = UNSET
    tariff: Union[Unset, None, int] = UNSET
    tariff_data: Union[Unset, VpnSubscriptionTariffData] = UNSET
    vpn_items: Union[Unset, List[VpnSubscriptionVpnItemsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user
        discount = self.discount
        status = self.status.value

        discounted_price = self.discounted_price
        pkid = self.pkid
        user_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_data, Unset):
            user_data = self.user_data.to_dict()

        tariff = self.tariff
        tariff_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tariff_data, Unset):
            tariff_data = self.tariff_data.to_dict()

        vpn_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vpn_items, Unset):
            vpn_items = []
            for vpn_items_item_data in self.vpn_items:
                vpn_items_item = vpn_items_item_data.to_dict()

                vpn_items.append(vpn_items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "discount": discount,
                "status": status,
                "discounted_price": discounted_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if tariff is not UNSET:
            field_dict["tariff"] = tariff
        if tariff_data is not UNSET:
            field_dict["tariff_data"] = tariff_data
        if vpn_items is not UNSET:
            field_dict["vpn_items"] = vpn_items

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        discount = (
            self.discount if isinstance(self.discount, Unset) else (None, str(self.discount).encode(), "text/plain")
        )
        status = (None, str(self.status.value).encode(), "text/plain")

        discounted_price = (
            self.discounted_price
            if isinstance(self.discounted_price, Unset)
            else (None, str(self.discounted_price).encode(), "text/plain")
        )
        pkid = self.pkid if isinstance(self.pkid, Unset) else (None, str(self.pkid).encode(), "text/plain")
        user_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.user_data, Unset):
            user_data = (None, json.dumps(self.user_data.to_dict()).encode(), "application/json")

        tariff = self.tariff if isinstance(self.tariff, Unset) else (None, str(self.tariff).encode(), "text/plain")
        tariff_data: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tariff_data, Unset):
            tariff_data = (None, json.dumps(self.tariff_data.to_dict()).encode(), "application/json")

        vpn_items: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.vpn_items, Unset):
            _temp_vpn_items = []
            for vpn_items_item_data in self.vpn_items:
                vpn_items_item = vpn_items_item_data.to_dict()

                _temp_vpn_items.append(vpn_items_item)
            vpn_items = (None, json.dumps(_temp_vpn_items).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "user": user,
                "discount": discount,
                "status": status,
                "discounted_price": discounted_price,
            }
        )
        if pkid is not UNSET:
            field_dict["pkid"] = pkid
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if tariff is not UNSET:
            field_dict["tariff"] = tariff
        if tariff_data is not UNSET:
            field_dict["tariff_data"] = tariff_data
        if vpn_items is not UNSET:
            field_dict["vpn_items"] = vpn_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        discount = d.pop("discount")

        status = VpnSubscriptionStatus(d.pop("status"))

        discounted_price = d.pop("discounted_price")

        pkid = d.pop("pkid", UNSET)

        _user_data = d.pop("user_data", UNSET)
        user_data: Union[Unset, VpnSubscriptionUserData]
        if isinstance(_user_data, Unset):
            user_data = UNSET
        else:
            user_data = VpnSubscriptionUserData.from_dict(_user_data)

        tariff = d.pop("tariff", UNSET)

        _tariff_data = d.pop("tariff_data", UNSET)
        tariff_data: Union[Unset, VpnSubscriptionTariffData]
        if isinstance(_tariff_data, Unset):
            tariff_data = UNSET
        else:
            tariff_data = VpnSubscriptionTariffData.from_dict(_tariff_data)

        vpn_items = []
        _vpn_items = d.pop("vpn_items", UNSET)
        for vpn_items_item_data in _vpn_items or []:
            vpn_items_item = VpnSubscriptionVpnItemsItem.from_dict(vpn_items_item_data)

            vpn_items.append(vpn_items_item)

        vpn_subscription = cls(
            user=user,
            discount=discount,
            status=status,
            discounted_price=discounted_price,
            pkid=pkid,
            user_data=user_data,
            tariff=tariff,
            tariff_data=tariff_data,
            vpn_items=vpn_items,
        )

        vpn_subscription.additional_properties = d
        return vpn_subscription

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
