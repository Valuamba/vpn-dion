from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.vpn_instance.serializers import VpnInstanceSerializer
from apps.vpn_item.models import VpnItem
from apps.vpn_protocol.serializers import VpnProtocolSerializer
# from apps.vpn_subscription.serializers import VpnBoundSubscription


class CreateVpnItemSerializer(serializers.ModelSerializer):
    pkid = serializers.IntegerField(read_only=True)

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(CreateVpnItemSerializer, self).__init__(many=many, *args, **kwargs)

    def validate_empty_values(self, data):
        return super(CreateVpnItemSerializer, self).validate_empty_values(data)

    class Meta:
        model = VpnItem
        fields = [
            'pkid',
            'instance',
            'protocol',
            'vpn_subscription'
        ]


class VpnItemSerializer(serializers.ModelSerializer):
    instance_data = VpnInstanceSerializer(many=False, read_only=True)
    protocol_data = VpnProtocolSerializer(many=False, read_only=True)

    class Meta:
        model = VpnItem
        fields = [
            'pkid',
            # 'vpn_subscription',
            # 'vpn_subscription_data'
            'instance',
            'instance_data',
            'protocol',
            'protocol_data',
            'public_key',
            'private_key',
            'address',
            'dns',
            'preshared_key',
            'endpoint',
            'allowed_ips',
            'config_name'
        ]


class VpnItemCreateSerializer(ModelSerializer):
    pkid = serializers.IntegerField(read_only=True)

    class Meta:
        model = VpnItem
        fields = [
            'pkid',
            "protocol",
            'instance'
        ]