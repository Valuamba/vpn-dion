from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.promocode.models import PromoCode


# Create your views here.


@api_view(['POST'])
def get_promocode_details(request):
    promocode = request.data.get('promocode')
    user_id = request.data.get('user_id')

    try:
        promocode_entity = PromoCode.objects.get(promocode=promocode, expires__gt=timezone.now())
    except PromoCode.DoesNotExist:
        return Response(data={ 'is_promocode_ready': False}, status=status.HTTP_200_OK)

    return Response(data={
        'discount': promocode_entity.discount,
        'promocode': promocode,
        'is_promocode_ready': promocode_entity.check_promocode(user_id)
    }, status=status.HTTP_200_OK)
