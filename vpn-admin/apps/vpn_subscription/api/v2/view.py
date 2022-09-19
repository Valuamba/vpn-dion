from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from apps.vpn_subscription.datatypes import PaymentState
from apps.vpn_subscription.selectors import get_default_protocol
from apps.vpn_subscription.service import create_subscription, create_payment_provider_link


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
        result.is_valid()

        return Response(data=result.validated_data, status=status.HTTP_201_CREATED)