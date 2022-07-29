from rest_framework import serializers

from apps.bot_users.models import BotUser


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        # fields = '__all__'
        exclude = ['id',]

    def validate_user_id(self, user_id):
        if BotUser.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError(f"User with user_id {user_id} already exists.")
        return user_id


class UpdateBotUserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fileds = ['language', 'role', 'user_name', 'first_name', 'last_name', 'is_bot_blocked']