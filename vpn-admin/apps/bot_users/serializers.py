from rest_framework import serializers

from apps.bot_users.models import BotUser


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
        exclude = ['id', 'pkid']


class UpdateBotUserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fileds = ['language', 'role', 'user_name', 'first_name', 'last_name', 'is_bot_blocked']