import pytest
from docker import APIClient
from mixer.backend.django import mixer as _mixer
from django.utils import timezone



@pytest.fixture
def protocol(mixer):
    return mixer.blend('vpn_protocol.VpnProtocol', pkid=1)


@pytest.fixture
def promo_code(mixer):
    return mixer.blend('promocode.PromoCode', pkid=1, promocode="OFF")


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api():
    return APIClient()

