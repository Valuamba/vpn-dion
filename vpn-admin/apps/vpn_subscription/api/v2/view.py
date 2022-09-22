from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_device_tariff.selectors import calculate_discounted_price
from apps.vpn_subscription.datatypes import PaymentState
from apps.vpn_subscription.models import VpnSubscription
from apps.vpn_subscription.selectors import get_default_protocol, get_subscription_by_id, get_one_device_tariffs
from apps.vpn_subscription.service import create_subscription, create_payment_provider_link, successful_subscription, \
    fail_subscription
from lib.serializer_utils import inline_serializer


class VpnSubscriptionCreateSingleDeviceApi(APIView):
    class InputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()
        tariff_id = serializers.IntegerField()
        country_id = serializers.IntegerField()
        promo_code = serializers.CharField(required=False)
        state = serializers.CharField(default=PaymentState.ExtendVpnSubscription, required=False)

    class OutputSerializer(serializers.Serializer):
        subscription_id = serializers.IntegerField()
        freekassa_url = serializers.CharField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        protocol = get_default_protocol()
        subscription = create_subscription(**serializer.validated_data, devices=[{
            'protocol_id': protocol.pkid,
            'country_id': serializer.validated_data.get('country_id')
        }])
        freekassa_url = create_payment_provider_link(
            subscription_id=subscription.id,
            state=serializer.validated_data.get('state'),
            payment_provider='Freekassa',
            promo_code=serializer.validated_data.get('promo_code'))

        data = {
            'subscription_id': subscription.pkid,
            'freekassa_url': freekassa_url
        }

        result = self.OutputSerializer(data=data)
        result.is_valid(raise_exception=True)

        return Response(data=result.validated_data, status=status.HTTP_201_CREATED)


class VpnSubscriptionDetails(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        user_data = inline_serializer(fields={
            'user_id': serializers.IntegerField(),
        })

        vpn_items_list = inline_serializer(many=True, fields={
            'country_data': inline_serializer(fields={
                'pkid': serializers.IntegerField(),
                'locale_ru': serializers.CharField(),
                'country': serializers.CharField(),
                'place': serializers.CharField(),
                'discount_percentage': serializers.CharField()
            }),

            'protocol_data': inline_serializer(fields={
                'pkid': serializers.IntegerField(),
                'protocol': serializers.CharField()
            }),
        })
        class Meta:
            model = VpnSubscription
            fields = [
                'pkid', 'month_duration', 'days_duration', 'devices_number', 'status',
                'is_referral', 'price', 'discount', 'subscription_end',
                'reminder_state', 'user_data', 'vpn_items_list', 'created_at', 'update_at',
            ]
    def get(self, request, subscription_id):
        subscription = get_subscription_by_id(subscription_id=subscription_id)

        serializer = self.OutputSerializer(subscription)

        return Response(serializer.data)


class VpnOneDeviceTariff(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        duration_data = inline_serializer(fields={
            'month_duration': serializers.IntegerField()
        })
        class Meta:
            model = VpnDeviceTariff
            fields = [
                'pkid', 'duration_data', 'total_discount', 'price'
            ]
    def get(self, request):
        tariffs = get_one_device_tariffs()

        serializer = self.OutputSerializer(tariffs, many=True)

        return Response(serializer.data)


class SuccessfulSubscriptionPayment(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.CharField(required=False)
        phone = serializers.CharField(required=False)
        sign = serializers.CharField(required=False)
        state = serializers.CharField()
        promo_code = serializers.CharField(required=False)
        amount = serializers.IntegerField()
        currency_id = serializers.IntegerField(required=False)
        subscription_id = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        successful_subscription(**serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class FailSubscription(APIView):
    def get(self, request, subscription_id):
        fail_subscription(subscription_id=subscription_id)

        return Response(status=status.HTTP_200_OK)
