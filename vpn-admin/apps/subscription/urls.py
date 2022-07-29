from django.urls import path

from apps.subscription.views import create_vpn_item, GetOnlineInstancesAPIView, calculate_total_price, \
    CreateSubscription, create_subscription

urlpatterns = [
    path('create/<int:user_id>/', create_vpn_item, name='create_vpn_item'),
    path('get-online-instances', GetOnlineInstancesAPIView.as_view(), name='get_online_instances'),
    path('totalPrice/', calculate_total_price, name="calculate_total_price"),
    path('addSubscription', create_subscription, name="add_subscription")
]
