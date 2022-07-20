from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.bot_users.serializers import UpdateBotUserSerialzier, BotUserSerializer
from apps.bot_users.exceptions import BotUserNotFound


class GetBotUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = BotUser.objects.get(user_id=user_id)
        except BotUser.DoesNotExist:
            raise BotUserNotFound
        serializer = BotUserSerializer(user, context={"request": user})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateBotUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UpdateBotUserSerialzier

    def patch(self, request, user_id):
        try:
            BotUser.objects.get(user_id=user_id)
        except BotUser.DoesNotExist:
            raise BotUserNotFound

        serializer = UpdateBotUserSerialzier(data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
