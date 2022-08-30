from django.urls import path

from apps.vpn_item.viewsets import get_vpn_item_qrcode

app_name = "vpn-item"

urlpatterns = [
    path('qrcode/<str:device_id>/', get_vpn_item_qrcode),
]