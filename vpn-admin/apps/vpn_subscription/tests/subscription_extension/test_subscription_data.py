import pytest

from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.selectors import get_subscription_by_id, get_available_protocols
from apps.vpn_subscription.service import successful_subscription_extension
from apps.vpn_subscription.some_logic import get_operating_system, is_windows
from django.utils import timezone

pytestmark = [pytest.mark.django_db]


def test_handle_outdated_sub(mocker, default_successful_sub_args, outdated_subscription, promo_code):
    mocker.patch('apps.vpn_subscription.service.get_subscription_by_id', return_value=outdated_subscription)
    mocker.patch('apps.vpn_subscription.utils.get_object_or_None', return_value=promo_code)

    with pytest.raises(Exception) as exc_info:
        successful_subscription_extension(**default_successful_sub_args)

    assert "Subscription 1 is outdated" in str(exc_info.value)


def test_sub_with_wrong_status(mocker, sub_with_wrong_status, promo_code, default_successful_sub_args):
    get_sub_by_id = mocker.patch('apps.vpn_subscription.service.get_subscription_by_id', return_value=sub_with_wrong_status)
    get_promo = mocker.patch('apps.vpn_subscription.utils.get_object_or_None', return_value=promo_code)

    with pytest.raises(Exception) as exc_info:
        successful_subscription_extension(**default_successful_sub_args)
    assert "has wrong status for extension" in str(exc_info.value)

    assert get_sub_by_id.called
    assert not get_promo.called


def test_referral_sub_extension(mocker, referral_sub, promo_code, default_successful_sub_args):
    get_sub_by_id = mocker.patch('apps.vpn_subscription.service.get_subscription_by_id', return_value=referral_sub)
    get_promo = mocker.patch('apps.vpn_subscription.utils.get_object_or_None', return_value=promo_code)

    with pytest.raises(Exception) as exc_info:
        successful_subscription_extension(**default_successful_sub_args)
    assert "with referral type cannot be extended" in str(exc_info.value)

    assert get_sub_by_id.called
    assert not get_promo.called

# Протестировать подписку без VpnItems

# def test_referral_sub_without_vpn_items()