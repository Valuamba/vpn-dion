from rest_framework import serializers

from apps.bot_locale.models import MessageLocale


class BotLocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageLocale
        fields = [
            'alias',
            'text'
        ]