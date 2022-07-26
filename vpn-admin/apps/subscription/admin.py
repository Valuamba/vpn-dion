from django.contrib import admin

# Register your models here.
from apps.subscription.models import VpnSubscription

admin.site.register(VpnSubscription)
