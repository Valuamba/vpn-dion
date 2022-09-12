from django import forms
from django.core.exceptions import ValidationError

from emoji_picker.widgets import EmojiPickerTextareaAdmin

from apps.bot_feedback.models import *


class AnswerMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Message
        fields = ['message_id', 'text', 'admin_message_photo', 'admin_message']
        widgets = {
            'admin_message': EmojiPickerTextareaAdmin()
        }

    def clean_admin_message(self):
        admin_message = self.cleaned_data['admin_message']
        if len(admin_message) == 0:
            raise ValidationError("Can't be empty!")

        return admin_message
        