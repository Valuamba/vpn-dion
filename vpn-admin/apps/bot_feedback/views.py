from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.bot_feedback.models import Message


# Create your views here.


@api_view(['POST'])
def add_feedback_message(request):
    data = request.data
    Message.objects.create(
        consumer_id=data['user_id'],
        message_id=data['message_id'],
        text=data['text']
    )
    return Response(status=status.HTTP_200_OK)