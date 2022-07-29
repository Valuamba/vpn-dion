import json

from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser
from apps.bot_users.serializers import UpdateBotUserSerialzier, BotUserSerializer
from apps.bot_users.exceptions import BotUserNotFound


class GetAllUsersAPIView(generics.ListAPIView):
    model = BotUser
    serializer_class = BotUserSerializer
    queryset = BotUser.objects.all()


class GetBotUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = BotUser.objects.get(user_id=user_id)
        except BotUser.DoesNotExist:
            raise BotUserNotFound
        serializer = BotUserSerializer(user, context={"request": user})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_user(request):
    serializer = BotUserSerializer(data=request.data, many=False)
    if not serializer.is_valid():
        return Response({"detail": "Add new user validation error"}, status=status.HTTP_403_FORBIDDEN)

    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBotUserAPIView(generics.CreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = BotUser.objects.get(user_id=data['user_id'])
        except BotUser.DoesNotExist:
            user = BotUser.objects.create(user_id=data['user_id'], user_name=data['user_name'],
                                       first_name=data['first_name'], last_name=data['last_name'])
            user.save()

        serializer = BotUserSerializer(user, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


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
