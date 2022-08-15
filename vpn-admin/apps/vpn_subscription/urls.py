from django.urls import path

from apps.vpn_subscription.view import create_subscription, config_files, fail_subscription, list_user_subscriptions
from apps.vpn_subscription.viewsets import UserSubscriptionViewSet

app_name = "subscription"

urlpatterns = [
    path('create-subscription', create_subscription),
    path('create-config', config_files, name='create-config'),
    path('fail-subscription/<str:subscription_id>', fail_subscription),
    path('user-subscriptions/<str:user_id>/', UserSubscriptionViewSet.as_view()),
]