from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    protocol_id = serializers.IntegerField()


class CalculatePaymnetDataSerializer(serializers.Serializer):
    duration_tariff_id = serializers.IntegerField()
    devices = DeviceSerializer(many=True)


class PaymentDetailsResponseSerializer(serializers.Serializer):
    initial_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = serializers.IntegerField()