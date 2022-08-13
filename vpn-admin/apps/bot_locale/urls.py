from django.urls import path

from apps.bot_locale.views import bulk_get_locales, GetMessageLocaleAPIView

urlpatterns = [
    path('bulk-locale', bulk_get_locales),
]