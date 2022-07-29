from django.contrib import admin

# Register your models here.
from apps.subscription.models import VpnSubscription, Instance, VpnItem


class InstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'pkid', 'ip_address', 'name', 'country', 'is_online', 'created_at', 'update_at']
    filter_horizontal = ('protocols', )


# class VpnItemAdmin(admin.ModelAdmin):


admin.site.register(Instance, InstanceAdmin)
admin.site.register(VpnItem)
admin.site.register(VpnSubscription)
