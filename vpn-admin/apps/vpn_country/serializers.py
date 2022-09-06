from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from apps.vpn_country.models import VpnCountry


class VpnCountrySerializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True, max_length=200)

    class Meta:
        model = VpnCountry
        fields = [
            'pkid',
            'country',
            'discount_percentage',
            'locale_ru'
        ]

