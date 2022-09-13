"""vpn-admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r"vpn-duration-price", VpnDurationPriceViewSet)
# router.register(r"vpn-country", VpnCountryViewSet)
# router.register(r"vpn-protocol", VpnProtocolViewSet)
# router.register(r"vpn-instance", VpnInstanceViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bot/', include('apps.bot.urls')),
    path('api/v1/tariff/', include('apps.vpn_tariffs.urls')),
    path('api/v1/vpn_order/', include('apps.vpn_order.urls')),
]

# urlpatterns = [
#
#     path(
#         "api/v1/redoc/",
#         TemplateView.as_view(
#             template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
#         ),
#         name="redoc",
#     ),
#     path("api/v1/openapi-schema", get_schema_view(), name="openapi-schema"),
#     path("api/v1/", include(router.urls)),
#     path('admin/metrics', TemplateView.as_view(template_name='admin/metrics/home.html')),
#     path('api/v1/feedback/', include('apps.bot.urls')),
#     path('api/v1/vpn_device_tariff/', include('apps.vpn_device_tariff.urls')),
#     path('api/v1/subscription/', include('apps.vpn_subscription.urls')),
#     path('api/v1/promocode/', include('apps.promocode.urls')),
#     path('api/v1/metrics/', include('apps.metrics.urls')),
#     path('api/v1/bot_locale/', include('apps.bot_locale.urls')),
#     path('api/v1/vpn-item/', include('apps.vpn_item.urls')),
#     path('api/v1/bot_user/', include('apps.bot_users.urls')),
#     path('payment_processing/', include('apps.payment_processing.urls')),
#     path('admin/', admin.site.urls),
#     # path('payment/', TemplateView.as_view(template_name='payment/payment_processing.html')),
#     path('sentry-debug/', trigger_error),
#     path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ] \
#               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
#               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

pass