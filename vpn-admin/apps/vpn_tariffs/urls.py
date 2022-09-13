from django.urls import path

from apps.vpn_tariffs.views import VpnDeviceTariffList

urlpatterns = [
    path('list', VpnDeviceTariffList.as_view()),
]