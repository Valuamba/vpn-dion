from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.vpn_order.models import VpnItem
from apps.vpn_order.selectors import get_subscription_by_uuid, get_subscription_device_list, get_vpn_item
from apps.vpn_order.services import create_subscription, create_payment_provider_link, generate_qr_code, \
    create_vpn_config_file, calculate_invoice
from apps.vpn_tariffs.selectors import calculate_discounted_price_with_devices
from lib.serializer_utilit import inline_serializer


# Create your views here.


class VpnSubscriptionCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()
        tariff_id = serializers.IntegerField()
        devices = inline_serializer(many=True, fields={
            'country_id': serializers.IntegerField(),
            'protocol_id': serializers.IntegerField()
        })
        promo_code = serializers.CharField(required=False)
        # state = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_subscription(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class ProviderLinkDetail(APIView):
    class InputSerializer(serializers.Serializer):
        state = serializers.CharField()
        subscription_id = serializers.UUIDField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_provider_url = create_payment_provider_link(**serializer.validated_data)
        return Response(data=payment_provider_url, status=status.HTTP_200_OK)


class SubscriptionDeviceList(APIView):
    class OutputSerializer(serializers.Serializer):
        vpn_item_id = serializers.IntegerField()
        country = serializers.CharField()
        protocol = serializers.CharField()

    def get(self, request, subscription_id):
        devices = get_subscription_device_list(subscription_id=subscription_id)

        data = self.OutputSerializer(data=devices, many=True)

        return Response(data)


class GenerateVpnConfigQRCode(APIView):
    def post(self, request, vpn_item_id):
        qr_code_b = generate_qr_code(vpn_item_id)
        return HttpResponse(qr_code_b.getvalue(), content_type="image/png")


class GenerateVpnConfig(APIView):
    def post(self, request, vpn_item_id):
        content = create_vpn_config_file(vpn_item_id=vpn_item_id)
        return HttpResponse(content, content_type="text/plain")


class VpnItemDetails(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VpnItem
            fields = [ 'pkid', 'protocol_name', 'country_name']

    def get(self, request, vpn_item_id):
        vpn_item = get_vpn_item(vpn_item_id=vpn_item_id)
        data = self.OutputSerializer(vpn_item)
        return Response(data)


class CalculateInvoice(APIView):
    class InputSerializer(serializers.Serializer):
        tariff_id = serializers.IntegerField()
        devices = inline_serializer(many=True, fields={
            'country_id': serializers.IntegerField(),
            'protocol_id': serializers.IntegerField()
        })
        promo_code = serializers.CharField(required=False)

    class OutputSerializer(serializers.Serializer):
        discount = serializers.IntegerField()
        price = serializers.IntegerField()
        
    def post(self, request):
            # logger.info(f'Calcaulate invoice for tariff {tariff_id} and {len(devices)} amount of devices')

            input_data = self.InputSerializer(data=request.data)
            input_data.is_valid()

            invoice = calculate_invoice(**input_data.validated_data)

            output_serializer = self.OutputSerializer()

            return Response(data={
                'discount': tariff.total_discount + promocode_discount,
                'price': total_price
            }, status=status.HTTP_200_OK
            )


