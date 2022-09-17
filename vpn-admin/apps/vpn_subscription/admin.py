from django.contrib import admin

from apps.vpn_item.models import VpnItem
from apps.vpn_subscription.models import VpnPaymentTransaction


class VpnPaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'email', 'phone', 'sign',
                    'price', 'currency_id', 'promocode',
                    'created_at', 'update_at']


admin.site.register(VpnPaymentTransaction, VpnPaymentTransactionAdmin)