from rest_framework import serializers

from apps.bot_assets.models import VpnCountry
from apps.bot_assets.serializers import VpnCountrySerializer, VpnProtocolSerializer
from apps.subscription.models import VpnSubscription, VpnItem, Instance


class VpnSubscriptionSerializer(serializers.ModelSerializer):
    # vpn_items = serializers.RelatedField(read_only=True)
    # country = CountryField(name_only=True)

    class Meta:
        model = VpnSubscription
        fields = '__all__'


class VpnItemSerializer(serializers.ModelSerializer):
    bot_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = VpnItem
        fields = '__all__'
        exclude = ['id', 'pkid']

    def get_bot_user(self, obj):
        return obj.bot_user.full_name


class InstanceSerializer(serializers.ModelSerializer):
    country = VpnCountrySerializer()
    protocols = VpnProtocolSerializer(many=True)

    class Meta:
        model = Instance
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=VpnCountry.objects.all())
    # selected_country_pkid = serializers.IntegerField()