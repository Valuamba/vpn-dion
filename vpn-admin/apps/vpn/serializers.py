from rest_framework import serializers

from apps.vpn.models import VpnItem


class VpnItemSerializer(serializers.ModelSerializer):
    bot_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = VpnItem
        fields = '__all__'
        exclude = ['id', 'pkid']

    def get_bot_user(self, obj):
        return obj.bot_user.full_name
