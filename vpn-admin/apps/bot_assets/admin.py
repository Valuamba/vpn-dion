from django.contrib import admin

# Register your models here.
from apps.bot_assets.models import VpnSubscriptionOffer, VpnCountry, VpnDurationPrice, VpnProtocol


class VpnSubscriptionOfferAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'devices_number', 'operation', 'discount_percentage']
    # ordering = ('-month_duration',)


class VpnCountryAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'country', 'discount_percentage']


class VpnDurationPriceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'price']


class VpnProtocolAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'protocol']


admin.site.register(VpnDurationPrice, VpnDurationPriceAdmin)
admin.site.register(VpnSubscriptionOffer, VpnSubscriptionOfferAdmin)
admin.site.register(VpnCountry, VpnCountryAdmin)
admin.site.register(VpnProtocol, VpnProtocolAdmin)