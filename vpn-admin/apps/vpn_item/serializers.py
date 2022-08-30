from rest_framework import serializers


class VpnItemCreateSerializer(serializers.Serializer):
    protocol_id = serializers.IntegerField(required=True, min_value=0)
    country_id = serializers.IntegerField(required=True, min_value=0)