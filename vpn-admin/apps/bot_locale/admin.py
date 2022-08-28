from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export import resources
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.forms import ImportForm

from apps.bot_locale.models import MessageLocale


class MessageLocaleResource(resources.ModelResource):
    class Meta:
        model = MessageLocale
        fields = (
            'alias',
            'text'
        )


class MessageLocaleAdmin(ExportActionMixin, ImportMixin, admin.ModelAdmin):
    list_display = ("alias", "text")
    resource_class = MessageLocaleResource

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 16, 'cols': 60})},
    }


admin.site.register(MessageLocale, MessageLocaleAdmin)