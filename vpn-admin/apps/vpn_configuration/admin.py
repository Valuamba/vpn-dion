from django.contrib import admin

# Register your models here.
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription

admin.site.register([VpnDurationPrice, VpnDeviceTariff, VpnCountry, VpnProtocol, VpnSubscription, VpnInstance])
# admin.site.register(VpnSubscriptionTariff)
