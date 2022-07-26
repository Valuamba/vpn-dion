from django.contrib import admin

# Register your models here.
from apps.vpn.models import VpnItem, VpnProduct

admin.site.register(VpnItem)
admin.site.register(VpnProduct)