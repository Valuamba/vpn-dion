import pytest

from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.selectors import get_subscription_by_id, get_available_protocols
from apps.vpn_subscription.service import successful_subscription_extension
from apps.vpn_subscription.some_logic import get_operating_system, is_windows

pytestmark = [pytest.mark.django_db]


# def test_get_subscription_by_id(subscription):
#     assert subscription.pkid == 1
#
#
# def test_vpn_subscription(mocker, subscription):
#     mocker.patch('apps.vpn_subscription.selectors.get_subscription_by_id', return_value=subscription)
#
#     s = get_subscription_by_id(subscription_id=9)
#
#     assert s.pkid == 1
#
#
# def test_get_available_protocols(mocker, protocol):
#     mocker.patch('apps.vpn_subscription.selectors.get_available_protocols', return_value=[protocol])
#     protocols = get_available_protocols()
#
#     assert protocols[0].pkid == 1


def test_get_operating_system(mocker, subscription, promo_code):
    mocker.patch('apps.vpn_subscription.service.get_subscription_by_id', return_value=subscription)

    mocker.patch('apps.vpn_subscription.utils.get_object_or_None', return_value=promo_code)

    successful_subscription_extension(
        email="jackjones@pr.com",
        subscription_id=1,
        amount=1000,
        promo_code="OFF",
        currency_id=4,
        phone="+4857463621",
        sign="klfdbfdb",
    )
    # w = is_windows()
    # assert is_windows() == True
    # assert get_operating_system() == "Linux"