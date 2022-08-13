import json

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.bot_locale.models import MessageLocale
from apps.bot_locale.serializers import BotLocaleSerializer


class GetMessageLocaleAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = MessageLocale.objects.all()
    serializer_class = BotLocaleSerializer


@api_view(['POST'])
def bulk_get_locales(request):
    aliases = request.data.get('aliases', None)

    if not aliases or len(aliases) == 0:
        formatted_response = {"detail": "There is no alias field."}
        return Response(formatted_response, status.HTTP_400_BAD_REQUEST)

    locales = {}
    for alias in aliases:
        try:
            locale = MessageLocale.objects.get(alias=alias)
            locales[locale.alias] = locale.text
        except MessageLocale.DoesNotExist:
            formatted_response = {"detail": f"Locale {alias} doesn't exist"}
            return Response(formatted_response, status.HTTP_400_BAD_REQUEST)

    return Response(data=locales, status=status.HTTP_200_OK)

