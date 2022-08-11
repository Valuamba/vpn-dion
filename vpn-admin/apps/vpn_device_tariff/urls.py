from django.urls import path

from apps.vpn_device_tariff.views import get_devices_result_payment_details

app_name = "vpn_device"

urlpatterns = [
    path('recalculate-payment-details', get_devices_result_payment_details)
]