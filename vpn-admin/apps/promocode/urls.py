from django.urls import path

from apps.promocode.views import get_promocode_details

urlpatterns = [
    path('details', get_promocode_details)
]