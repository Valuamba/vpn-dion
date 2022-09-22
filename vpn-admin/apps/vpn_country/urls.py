from django.urls import path

from apps.vpn_country.view import VpnCountryList

app_name = "vpn-country"

urlpatterns = [
    path('available', VpnCountryList.as_view())
]