from apps.vpn_country.models import VpnCountry
from apps.vpn_protocol.models import VpnProtocol


def get_default_country() -> VpnCountry:
    return VpnCountry.get_defaults()[0]


def get_default_protocol() -> VpnProtocol:
    return VpnProtocol.get_defaults()[0]