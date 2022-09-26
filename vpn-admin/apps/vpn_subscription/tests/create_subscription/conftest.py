import pytest
from dateutil.relativedelta import relativedelta
from docker import APIClient
from mixer.backend.django import mixer as _mixer
from django.utils import timezone

from apps.vpn_subscription.models import SubscriptionPaymentStatus


@pytest.fixture
def outdated_subscription(mixer):
    return mixer.blend('vpn_subscription.VpnSubscription', pkid=1,
                       subscription_end=timezone.now() + relativedelta(days=-7))


@pytest.fixture
def sub_with_wrong_status(mixer):
    return mixer.blend('vpn_subscription.VpnSubscription', pkid=1,
                       subscription_end=timezone.now() + relativedelta(days=30),
                       status=SubscriptionPaymentStatus.WAITING_FOR_PAYMENT)


@pytest.fixture
def default_successful_sub_args():
    return {
        'email': "jackjones@pr.com",
        'subscription_id': 1,
        'amount': 1000,
        'promo_code': "OFF",
        'currency_id': 4,
        'phone': "+4857463621",
        'sign': "klfdbfdb"
    }
