from django.urls import path

from apps.vpn_subscription.view import create_subscription, successful_payment, fail_subscription, \
    list_user_subscriptions, \
    activate_referral_subscription, calculate_invoice, successful_subscription_extension, get_subscription_checkout, \
    activate_invited_user_trial_subscription, get_user_active_subscriptions, check_subscription_extension

app_name = "subscription"

urlpatterns = [
    path('get-subscription-checkout/<str:subscription_id>', get_subscription_checkout),
    path('create-subscription', create_subscription),
    path('invited-user-subscription', activate_invited_user_trial_subscription),
    path('successful-subscription-extension', successful_subscription_extension),
    path('successful-payment', successful_payment, name='create-config'),
    path('create-referral-subscription', activate_referral_subscription, name='create-referral'),
    path('fail-subscription/<str:subscription_id>', fail_subscription),
    path('user-subscriptions/<str:user_id>/', list_user_subscriptions),
    path('user-active-subscriptions/<str:user_id>/', get_user_active_subscriptions),
    path('calculate-invoice', calculate_invoice),
    path('check_subscription_extension/<str:subscription_id>', check_subscription_extension),
]