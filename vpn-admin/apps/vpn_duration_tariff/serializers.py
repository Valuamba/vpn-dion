from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.vpn_duration_tariff.models import VpnDurationPrice


class VpnDurationPriceSerializer(ModelSerializer):
    currency = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        model = VpnDurationPrice
        fields = [
            'pkid',
            'month_duration',
            'currency',
            'amount'
        ]