from django.urls import path

from apps.vpn_subscription.view import create_subscription, config_files

app_name = "subscription"

urlpatterns = [
    path('create-subscription', create_subscription),
    path('create-config', config_files, name='create-config')
]