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
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from apps.bot_users.viewsets import BotUserViewSet
from apps.vpn_country.viewsets import VpnCountryViewSet
from apps.vpn_device_tariff.views import VpnDeviceTariffViewSet
from apps.vpn_duration_tariff.viewsets import VpnDurationPriceViewSet
from apps.vpn_item.viewsets import VpnItemViewSet
from apps.vpn_protocol.viewsets import VpnProtocolViewSet
from apps.vpn_subscription.viewsets import VpnSubscriptionViewSet

router = DefaultRouter()
router.register(r"vpn-duration-price", VpnDurationPriceViewSet)
router.register(r"vpn-device-tariff", VpnDeviceTariffViewSet)
router.register(r"vpn-country", VpnCountryViewSet)
router.register(r"vpn-protocol", VpnProtocolViewSet)
router.register(r"vpn-subscription", VpnSubscriptionViewSet)
router.register(r"vpn-item", VpnItemViewSet)
router.register(r"bot-user", BotUserViewSet)

urlpatterns = [

    path(
        "api/v1/redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    path("api/v1/openapi-schema", get_schema_view(), name="openapi-schema"),
    path("api/v1/", include(router.urls)),
    # path("api/v1/subscription", include('apps.vpn_subscription.urls')),


    # path('admin/metrics', TemplateView.as_view(template_name='admin/metrics/home.html')),
    path('admin/metrics', TemplateView.as_view(template_name='admin/metrics/home.html')),
    path('api/v1/metrics/', include('apps.metrics.urls')),
    path('admin/', admin.site.urls),
    # path('api/v1/bot_user/', include('apps.bot_users.urls')),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    #
    # path("api/v1/auth/", include("djoser.urls")),
    # path("api/v1/auth/", include("djoser.urls.jwt")),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

pass