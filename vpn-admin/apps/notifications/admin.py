from django.contrib import admin

from apps.notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'status', 'schedule_time', 'was_sent', 'created_at', 'update_at']


admin.site.register(Notification, NotificationAdmin)
