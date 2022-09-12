from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.bot.models import BotUser
from apps.bot.selectors import get_user_by_id, bulk_get_locales, get_locale, get_referral_data
from apps.bot.services import add_feedback_message, add_bot_user


class FeedbackMessageCreate(APIView):
    class InputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()
        message_id = serializers.IntegerField()
        text = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        add_feedback_message(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class MessageLocaleRetrieve(APIView):
    def get(self, request, alias):
        locale = get_locale(alias=alias)
        return Response(data=locale)


class MessageLocaleBulkList(APIView):
    class InputSerializer(serializers.Serializer):
        aliases = serializers.ListField(child=serializers.CharField())

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        locales = bulk_get_locales(**serializer.validated_data)

        return Response(data=locales, status=status.HTTP_200_OK)


class BotUserDetails(APIView):
    class OutputSerializer(serializers.Serializer):
        class Meta:
            model = BotUser
            fields = [ 'user_id', 'first_name', 'user_name', 'last_name', 'is_bot_blocked', 'referral_value', 'referral_link']

    def post(self, request, user_id):
        user = get_user_by_id(user_id=user_id)
        data = self.OutputSerializer(data=user)
        return Response(data)


class BotUserCreate(APIView):
    class InputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()
        user_name = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        referral_value = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        add_bot_user(**serializer.validated_data)


class BotUserReferralDetails(APIView):
    class OutputSerializer(serializers.Serializer):
        referral_link = serializers.CharField()
        count_referrals = serializers.CharField()
        count_free_month_subscription = serializers.CharField()

    def get(self, user_id):
        referral_details = get_referral_data(user_id=user_id)
        data = self.OutputSerializer(data=referral_details)
        return Response(data)




