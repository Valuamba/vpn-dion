from django.contrib import admin
from apps.vpn_tariffs.models import VpnDeviceTariff, VpnDurationPrice

# Register your models here.


class VpnDurationPriceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'month_duration', 'price']


class VpnDeviceTariffsAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'duration', 'devices_number', 'operation', 'discount_percentage']


admin.site.register(VpnDeviceTariff, VpnDeviceTariffsAdmin)
admin.site.register(VpnDurationPrice, VpnDurationPriceAdmin)