from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from apps.bot_users.exceptions import BotUserNotFound
from apps.bot_users.models import BotUser


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_vpn_item(request, user_id):
    try:
        bot_user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound


