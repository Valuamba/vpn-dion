from rest_framework import serializers


class CreateBotUserRequest(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=200, allow_blank=True)
    first_name = serializers.CharField(max_length=200, allow_blank=True)
    last_name = serializers.CharField(max_length=200, allow_blank=True)
    referral_value = serializers.CharField(max_length=200, allow_null=True, required=False)


class UpdateBotUserRequest(serializers.Serializer):
    user_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    first_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    last_name = serializers.CharField(max_length=200, allow_null=True, required=False)
    referral_value = serializers.CharField(max_length=200, allow_null=True, required=False)




