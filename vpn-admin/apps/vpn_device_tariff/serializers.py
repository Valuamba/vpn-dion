from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.serializers import VpnDurationPriceSerializer


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