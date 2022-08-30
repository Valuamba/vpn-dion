
from rest_framework import serializers
from apps.vpn_item.serializers import VpnItemCreateSerializer


class PaymentDetailsResponseSerializer(serializers.Serializer):
    initial_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discounted_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = serializers.IntegerField()


class CreateSubscriptionSerilizer(serializers.Serializer):
    tariff_id = serializers.IntegerField(required=True, min_value=0)
    user_id = serializers.IntegerField(required=True, min_value=0)
    devices = VpnItemCreateSerializer(required=True, many=True)

    def validated_data(self):
        devices = self.data['devices']
        if len(devices) == 0:
            raise 'Devices cannot be empty'


class CreateSubscriptionConfigsRequest(serializers.Serializer):
    subscription_id = serializers.IntegerField(required=True, min_value=0)