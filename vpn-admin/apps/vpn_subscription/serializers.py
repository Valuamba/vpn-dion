import json

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.bot_users.serializers import BotUserSerializer
from apps.vpn_device_tariff.serializers import VpnDeviceTariffSerializer
from apps.vpn_item.models import VpnItem
from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.models import VpnSubscription


class VpnSubscriptionSerializer(serializers.ModelSerializer):
    user_data = BotUserSerializer(read_only=True, many=False)
    tariff_data = VpnDeviceTariffSerializer(read_only=True, many=False)
    vpn_items = VpnItemCreateSerializer(many=True, read_only=True)

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
        ]

    def create(self, validated_data):
        vpn_items = validated_data.pop('vpn_items', None)
        vpn_subscription = super().create(validated_data)

        new_vpn_items = []
        for vpn_item in vpn_items:
            new_vpn_item = VpnItemCreateSerializer().create({
                    **vpn_item,
                    'vpn_subscription_id': vpn_subscription.pkid
                })
            new_vpn_items.append(new_vpn_item.id)

        return vpn_subscription


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
