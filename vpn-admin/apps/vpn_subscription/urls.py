from django.urls import path

from apps.vpn_subscription.view import create_subscription, calculate_payment_details

app_name = "subscription"

urlpatterns = [
    path('create-subscription', create_subscription),
    path('calculate-payment', calculate_payment_details),
]