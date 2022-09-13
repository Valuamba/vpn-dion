from django.contrib import admin

from apps.vpn_order.models import VpnInstance, VpnCountry, VpnProtocol, VpnSubscription, VpnItem


class VpnInstanceAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'ip_address', 'port', 'mac', 'name', 'country', 'is_online', 'created_at', 'update_at']
    filter_horizontal = ('protocols', )


class VpnCountryAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'place', 'locale_ru', 'discount_percentage', 'is_default']


class VpnProtocolAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'name', 'is_default']


class VpnSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'user', 'status', 'is_referral']


class VpnItemAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'country_name', 'protocol_name', 'public_key', 'private_key', 'address', 'dns', 'preshared_key', "endpoint", "allowed_ips", "config_name"]


admin.site.register(VpnItem, VpnItemAdmin)
admin.site.register(VpnInstance, VpnInstanceAdmin)
admin.site.register(VpnCountry, VpnCountryAdmin)
admin.site.register(VpnProtocol, VpnProtocolAdmin)
admin.site.register(VpnSubscription, VpnSubscriptionAdmin)