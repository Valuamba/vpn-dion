from django.contrib import admin

from apps.promocode.models import PromoCode


# Register your models here.


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'promocode', 'discount', 'count_users', 'expires']
    readonly_fields=("applied_by_users", )


admin.site.register(PromoCode, PromoCodeAdmin)