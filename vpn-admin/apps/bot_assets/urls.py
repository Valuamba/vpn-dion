from django.urls import path

from apps.bot_assets.views import default_vpn_subscription_offer, GetAllDurationPricesAPIView, \
    GetAllVpnCountrySerializerAPIView, GetAllVpnSubscriptionOffersAPIView, GetAllActiveVpnCountrySerializerAPIView, \
    GetActiveProtocolsAPIView
from apps.subscription.views import create_vpn_item

urlpatterns = [
    path('dump', default_vpn_subscription_offer, name='create_vpn_item'),
    path('prices', GetAllDurationPricesAPIView.as_view(), name="get_all_prices"),
    path('offers', GetAllVpnSubscriptionOffersAPIView.as_view(), name="get_all_offers"),
    path('countries', GetAllVpnCountrySerializerAPIView.as_view(), name="get_all_countries"),
    path('active-countries', GetAllActiveVpnCountrySerializerAPIView.as_view(), name="get_active_countries"),
    path('active-protocols', GetActiveProtocolsAPIView.as_view(), name="get_active_countries"),
]