import json

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.bot_users.serializers import BotUserSerializer
from apps.vpn_device_tariff.serializers import VpnDeviceTariffSerializer, DeviceSerializer
from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemCreateSerializer, VpnItemSerializer
from apps.vpn_subscription.models import VpnSubscription


class UpdateVpnSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnSubscription
        fields = [
            'status'
        ]


class VpnSubscriptionSerializer(serializers.ModelSerializer):
    user_data = BotUserSerializer(read_only=True, many=False)
    tariff_data = VpnDeviceTariffSerializer(read_only=True, many=False)
    vpn_items = VpnItemSerializer(many=True, read_only=True)
    # initial_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = VpnSubscription
        fields = [
            'pkid',
            'user',
            'user_data',
            'tariff',
            'tariff_data',
            # 'total_price',
            'discount',
            'status',
            'vpn_items',
            # 'discounted_price',
            # 'discount'
        ]


class ReadVpnSubscriptionSerializer(serializers.ModelSerializer):
    user_data = BotUserSerializer(read_only=True, many=False)
    tariff_data = VpnDeviceTariffSerializer(read_only=True, many=False)

    class Meta:
        model = VpnSubscription
        fields = [
            'pkid',
            'user',
            'user_data',
            'tariff',
            'tariff_data',
            'total_price',
            'discount',
            'status',
            'vpn_items'
            'vpn_items_data'
        ]


class VpnBoundSubscription(serializers.ModelSerializer):
    vpn_subscription_data = VpnSubscriptionSerializer(many=False, read_only=True)


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