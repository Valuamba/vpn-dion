from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notifications.models import Notification


@api_view(['GET'])
def add_job(request):
    Notification.objects.create(
        text='sdvsd',
        schedule_time=timezone.now() + timezone.timedelta(seconds=15)
    )

    return Response(status=status.HTTP_200_OK)

