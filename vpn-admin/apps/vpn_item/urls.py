from django.urls import path

from apps.vpn_item.viewsets import get_vpn_item_qrcode, get_subscription_vpn_items, get_vpn_item_info, \
    get_vpn_config_file

app_name = "vpn-item"

urlpatterns = [
    path('qrcode/<str:device_id>/', get_vpn_item_qrcode),
    path('<str:vpn_item_id>/', get_vpn_item_info),
    path('config/<str:vpn_item_id>/', get_vpn_config_file),
    path('list_with_subscription/<str:subscription_id>', get_subscription_vpn_items)
]