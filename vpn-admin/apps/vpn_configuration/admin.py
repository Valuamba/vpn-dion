from django.contrib import admin

# Register your models here.
from apps.vpn_country.models import VpnCountry
from apps.vpn_device_tariff.models import VpnDeviceTariff
from apps.vpn_duration_tariff.models import VpnDurationPrice
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol
from apps.vpn_subscription.models import VpnSubscription


class VpnInstanceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'ip_address', 'port', 'mac', 'name', 'country', 'is_online', 'created_at', 'update_at']
    filter_horizontal = ('protocols', )


class VpnDeviceTariffsAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'duration', 'devices_number', 'operation', 'discount_percentage']


class VpnCountryAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'place', 'discount_percentage']


class VpnProtocolAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'protocol']


class VpnDurationPriceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'month_duration', 'price']


class VpnSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'user', 'status']


admin.site.register(VpnInstance, VpnInstanceAdmin)
admin.site.register(VpnDeviceTariff, VpnDeviceTariffsAdmin)
admin.site.register(VpnCountry, VpnCountryAdmin)
admin.site.register(VpnProtocol, VpnProtocolAdmin)
admin.site.register(VpnDurationPrice, VpnDurationPriceAdmin)
admin.site.register(VpnSubscription, VpnSubscriptionAdmin)
