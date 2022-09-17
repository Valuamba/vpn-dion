from django.contrib import admin

from apps.vpn_item.models import VpnItem


class VpnItemAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'public_key', 'private_key', 'address', 'dns',
                    'preshared_key', 'endpoint', 'allowed_ips', 'config_name',
                    'status', 'created_at', 'update_at']


admin.site.register(VpnItem, VpnItemAdmin)
