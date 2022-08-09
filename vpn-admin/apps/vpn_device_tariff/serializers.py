from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.vpn_country.models import VpnCountry
from apps.vpn_country.serializers import VpnCountrySerializer
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.serializers import VpnDurationPriceSerializer
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class VpnDeviceTariffSerializer(ModelSerializer):
    duration_data = VpnDurationPriceSerializer(read_only=True, many=False)
    result_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = VpnDeviceTariff
        fields = [
            "pkid",
            "duration",
            'duration_data',
            "devices_number",
            'operation',
            'discount_percentage',
            'result_price'
        ]


class DeviceSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    protocol_id = serializers.IntegerField()

    # country = VpnCountrySerializer()
    # protocol = VpnProtocolSerializer()
    #
    # country = serializers.StringRelatedField()
    # protocol = serializers.StringRelatedField()
    #
    # def country(self, obj):
    #     s = obj
    #
    # def get_protocol(self, obj):
    #     s1 = obj



    # country_id = serializers.IntegerField()
    # protocol_id = serializers.IntegerField()