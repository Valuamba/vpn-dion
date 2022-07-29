from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.bot_assets.models import VpnDurationPrice, VpnSubscriptionOffer, VpnCountry, VpnProtocol


class VpnDurationPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnDurationPrice
        fields = ['pkid', 'id', 'month_duration', 'price_currency', 'price']


class VpnSubscriptionOffersSerializer(serializers.ModelSerializer):
    # month_duration = serializers.SerializerMethodField()
    duration = VpnDurationPriceSerializer()

    class Meta:
        model = VpnSubscriptionOffer
        fields = ['pkid', 'duration', 'devices_number', 'operation', 'discount_percentage']

    # def get_month_duration(self, obj):
    #     return obj.duration.month_duration


class VpnCountrySerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = VpnCountry
        fields = '__all__'

    def get_country(self, country):
        return country


class VpnProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = VpnProtocol
        fields = '__all__'