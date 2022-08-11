from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.vpn_country.models import VpnCountry
from apps.vpn_country.serializers import VpnCountrySerializer
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.serializers import VpnDurationPriceSerializer
from apps.vpn_protocol.serializers import VpnProtocolSerializer


class DeviceSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    protocol_id = serializers.IntegerField()


class VpnDeviceTariffSerializer(ModelSerializer):
    duration_data = VpnDurationPriceSerializer(read_only=True, many=False)
    initial_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = serializers.StringRelatedField()
    total_discount = serializers.DecimalField(max_digits=10, decimal_places=2)
    devices = DeviceSerializer(write_only=True, default=[])

    class Meta:
        model = VpnDeviceTariff
        fields = [
            "pkid",
            "duration",
            'duration_data',
            "devices_number",
            'operation',
            'discount_percentage',
            'total_discount',
            'initial_price',
            'discounted_price',
            'devices'
        ]

    def get_discounted_price(self, obj):
        return self.model.discounted_price()


class CalculatePaymnetDataSerializer(serializers.Serializer):
    duration_tariff_id = serializers.IntegerField()
    devices = DeviceSerializer(many=True)


class PaymentDetailsResponseSerializer(serializers.Serializer):
    initial_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = serializers.IntegerField()