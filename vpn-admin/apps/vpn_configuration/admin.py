from django.contrib import admin

# Register your models here.
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription


class VpnInstanceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'ip_address', 'port', 'name', 'country', 'is_online', 'created_at', 'update_at']
    filter_horizontal = ('protocols', )


admin.site.register(VpnInstance, VpnInstanceAdmin)
admin.site.register([VpnDurationPrice, VpnDeviceTariff, VpnCountry, VpnProtocol, VpnSubscription])
# admin.site.register(VpnSubscriptionTariff)
