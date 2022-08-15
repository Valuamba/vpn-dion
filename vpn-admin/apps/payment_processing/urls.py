from django.urls import path

from apps.payment_processing.views import get_payment_checkout

app_name = 'payment_processing'

urlpatterns = [
    path('checkout/', get_payment_checkout)
]