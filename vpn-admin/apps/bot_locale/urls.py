from django.urls import path

from apps.bot_locale.views import bulk_get_locales, get_locale

urlpatterns = [
    path('bulk-locale', bulk_get_locales),
    path('locale/<str:alias>', get_locale),
]