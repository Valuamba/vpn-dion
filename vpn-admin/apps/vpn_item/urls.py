from django.urls import path

from apps.vpn_item.viewsets import SubscriptionVpnItemsViewSet, get_vpn_item_qrcode

app_name = "vpn-item"

urlpatterns = [
    path('subscription-vpn/<str:subscription_id>/', SubscriptionVpnItemsViewSet.as_view()),
    path('qrcode/<str:device_id>/', get_vpn_item_qrcode),
]