from django.urls import path

from apps.vpn_subscription.api.v2.view import VpnSubscriptionCreateSingleDeviceApi

urlpatterns = [
    # path('qrcode/<str:device_id>/', GenerateVpnConfigQRCode.as_view()),
    # path('<str:vpn_item_id>/', VpnItemDetails.as_view()),
    # path('config/<str:vpn_item_id>/', GenerateVpnConfig.as_view()),
    # path('subscription/list/<str:subscription_id>', SubscriptionDeviceList),

    path('single-device-create', VpnSubscriptionCreateSingleDeviceApi.as_view()),
    # path('provider-link', ProviderLinkDetail.as_view()),
]