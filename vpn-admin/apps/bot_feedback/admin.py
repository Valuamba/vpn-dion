from django.contrib import admin
from django.utils import timezone

from lib.telegram import TelegramClient
from .filters.admin_filters import StatusListFilter
from .forms import AnswerMessageForm
from .models import *


@admin.register(Message)
class MessageConfig(admin.ModelAdmin):
    readonly_fields = ('consumer', 'message_id', 'text', 'receive_date', 'answer_date')
    list_display = ('__str__', 'consumer', 'status', 'receive_date')
    list_filter = (('status', StatusListFilter),)
    
    form = AnswerMessageForm
    
    fieldsets = (
        (None, {
             'fields': (
                 'text',
                 # 'receive_date',
                 # 'admin_message_photo',
                 'admin_message',
                 'answer_date'
             )
         }),
    )
    
    actions = []
 
    show_save_and_continue = False
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return obj is not None and obj.status is None

    def has_delete_permission(self, request, obj=None):
        return obj is not None and obj.status is None

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        return super(MessageConfig, self).changeform_view(request, object_id, extra_context=extra_context)
    
    """Ignore message without deleting"""
    def delete_model(self, request, obj):
        obj.status = False
        obj.save()

    def save_model(self, request, obj, form, change):
        client = TelegramClient(settings.BOT_TOKEN, settings.TELEGRAM_API_ORIGIN)

        if obj.admin_message_photo:
            client.send_image(obj.consumer.user_id, obj.admin_message_photo.file,
                              reply_to_message_id=obj.message_id,
                              caption=obj.admin_message,
                              allow_sending_without_reply=False)
        else:
            client.send_message(obj.consumer.user_id, text=obj.admin_message,
                              reply_to_message_id=obj.message_id,
                              allow_sending_without_reply=False)
        obj.status = True
        obj.answer_date = timezone.now()
        super(MessageConfig, self).save_model(request, obj, form, change)
    
    def delete_view(self, request, object_id, extra_context=None):
        request.POST = {'post': ['yes']}
        return super(MessageConfig, self).delete_view(request, object_id, extra_context)
    