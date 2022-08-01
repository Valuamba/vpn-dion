from rest_framework import serializers

from apps.vpn_protocol.models import VpnProtocol


class VpnProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnProtocol
        fields = [
            'pkid',
            'protocol'
        ]
