from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from apps.bot_locale.models import MessageLocale
from apps.bot_locale.serializers import BotLocaleSerializer


class GetMessageLocaleAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = MessageLocale.objects.all()
    serializer_class = BotLocaleSerializer