from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from apps.bot_locale.models import MessageLocale


class MessageLocaleAdmin(admin.ModelAdmin):
    list_display = ("alias", "text")
    # readonly_fields = ('alias',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 16, 'cols': 60})},
    }


admin.site.register(MessageLocale, MessageLocaleAdmin)