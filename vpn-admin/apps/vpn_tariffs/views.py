from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.vpn_tariffs.selectors import get_tariffs_details


# Create your views here.


class VpnDeviceTariffList(APIView):
    class OutputSerializer(serializers.Serializer):
        tariff_id = serializers.IntegerField()
        month_duration = serializers.IntegerField()
        month_loc = serializers.CharField()
        devices_number = serializers.IntegerField()
        devices_loc = serializers.CharField()
        price = serializers.IntegerField()
        currency = serializers.CharField()
        discount = serializers.IntegerField()

    def get(self):
        tariffs = get_tariffs_details()
        data = self.OutputSerializer(tariffs, many=True)
        return Response(data)