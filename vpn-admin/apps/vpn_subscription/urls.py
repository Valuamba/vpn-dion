from django.urls import path

from apps.vpn_subscription.view import create_subscription

app_name = "subscription"

urlpatterns = [
    path('create-subscription', create_subscription)
]