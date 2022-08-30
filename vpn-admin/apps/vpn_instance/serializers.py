from rest_framework.serializers import ModelSerializer

from apps.vpn_country.serializers import VpnCountrySerializer
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class VpnInstanceSerializer(ModelSerializer):
    country_data = VpnCountrySerializer(many=False, read_only=True)
    protocols_data = VpnProtocolSerializer(many=True, read_only=False)

    class Meta:
        model = VpnInstance
        fields = [
            'pkid',
            'ip_address',
            'name',
            'country',
            'country_data',
            'protocols',
            'protocols_data',
            'is_online'
        ]