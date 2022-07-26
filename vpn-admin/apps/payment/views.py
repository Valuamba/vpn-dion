from datetime import datetime, timezone
from typing import List

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
@transaction.atomic
def get_payment_checkout():
    freekassa_url = "https://pay.freekassa.ru/?" \
                    "m=312" \
                    "&oa=1000" \
                    "&i=" \
                    "&currency=RUB" \
                    "&o=BALANCE_377&pay=PAY" \
                    "&s=e78c7ec7e87c"

