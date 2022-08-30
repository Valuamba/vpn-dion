from typing import List

import requests
import urllib3
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.vpn_instance.models import VpnInstance


def home_view(request):
    return render(request, "home.html")


@api_view(['GET'])
def collect_statistics(request):
    instances: List[VpnInstance] = VpnInstance.objects.all()
    statistics = []
    port = 5000
    for i in instances:
        is_online = i.is_online
        response = None
        stat = {
            "instance": i.name,
            "ip_address": i.ip_address,
            "is_online": is_online,
            "country": i.country_data.country,
        }
        if i.is_online:
            try:
                response = requests.get(f"http://{i.ip_address}:{port}/collect-statistics",
                                        timeout=3)
            except requests.exceptions.ConnectTimeout:
                is_online = False

        data = {}
        if response:
            data = response.json()

        stat = {
            **stat,
            "cpu": data.get('cpu', 0),
            "ram": data.get('ram', 0),
            "upload": data.get('upload', 0),
            "download": data.get('download', 0),
        }

        statistics.append(stat)

    return Response(data=statistics, status=status.HTTP_200_OK)