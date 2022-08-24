from rest_framework import serializers

from apps.bot_users.models import BotUser, ReferralItem


class ReferralItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralItem
        fields = ['referral_owner', 'referred_user', 'is_activated_reward']


class BotUserSerializer(serializers.ModelSerializer):
    # referrals = ReferralItemSerializer(many=True, read_only=True)
    # referral_item = ReferralItemSerializer(many=False, read_only=True)

    class Meta:
        model = BotUser
        fields = [
            'user_id',
            'user_name',
            'first_name',
            'last_name',
            'is_bot_blocked',
            # 'referrals',
            # 'referral_item'
        ]

    # def validate_user_id(self, user_id):
    #     if BotUser.objects.filter(user_id=user_id).exists():
    #         raise serializers.ValidationError(f"User with user_id {user_id} already exists.")
    #     return user_id


class UpdateBotUserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fileds = ['language', 'role', 'user_name', 'first_name', 'last_name', 'is_bot_blocked']


class CreateBotUserRequest(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=200, allow_blank=True)
    first_name = serializers.CharField(max_length=200, allow_blank=True)
    last_name = serializers.CharField(max_length=200, allow_blank=True)
    referral_value = serializers.CharField(max_length=200, allow_blank=True, required=False)


class UpdateBotUserRequest(serializers.Serializer):
    user_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    first_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    last_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    referral_value = serializers.CharField(max_length=200, allow_null=True, required=False)




