from django.urls import path

from apps.vpn_order.views import GenerateVpnConfigQRCode, VpnSubscriptionCreateApi, ProviderLinkDetail, \
    SubscriptionDeviceList, GenerateVpnConfig, VpnItemDetails

urlpatterns = [
    path('qrcode/<str:device_id>/', GenerateVpnConfigQRCode.as_view()),
    path('<str:vpn_item_id>/', VpnItemDetails.as_view()),
    path('config/<str:vpn_item_id>/', GenerateVpnConfig.as_view()),
    path('subscription/list/<str:subscription_id>', SubscriptionDeviceList),

    path('subscription/create', VpnSubscriptionCreateApi.as_view()),
    path('provider-link', ProviderLinkDetail.as_view()),

    # path('get-subscription-checkout/<str:subscription_id>', get_subscription_checkout),
    # path('invited-user-subscription', activate_invited_user_trial_subscription),
    # path('successful-subscription-extension', successful_subscription_extension),
    # path('successful-payment', successful_payment, name='create-config'),
    # path('create-referral-subscription', activate_referral_subscription, name='create-referral'),
    # path('fail-subscription/<str:subscription_id>', fail_subscription),
    # path('user-subscriptions/<str:user_id>/', list_user_subscriptions),
    # path('user-active-subscriptions/<str:user_id>/', get_user_active_subscriptions),
    # path('calculate-invoice', calculate_invoice),
    # path('check_subscription_extension/<str:subscription_id>', check_subscription_extension),
]