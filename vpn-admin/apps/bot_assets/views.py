from django.db import transaction
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from djmoney.money import Money
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.bot_assets.models import VpnSubscriptionOffer, VpnDurationPrice, VpnCountry, VpnProtocol
from apps.bot_assets.serializers import VpnDurationPriceSerializer, \
    VpnSubscriptionOffersSerializer, VpnCountrySerializer, VpnProtocolSerializer


@api_view(['POST'])
@transaction.atomic
def default_vpn_subscription_offer(request):
    VpnDurationPrice.objects.bulk_create([
        VpnDurationPrice(month_duration=1, price=Money(290.0, 'RUB')),
        VpnDurationPrice(month_duration=6, price=Money(890.0, 'RUB')),
        VpnDurationPrice(month_duration=12, price=Money(1490.0, 'RUB')),
    ])

    VpnSubscriptionOffer.objects.bulk_create([
        VpnSubscriptionOffer(month_duration=1, devices_number=1, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=0),
        VpnSubscriptionOffer(month_duration=1, devices_number=2, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=15),
        VpnSubscriptionOffer(month_duration=1, devices_number=3, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=20),
        VpnSubscriptionOffer(month_duration=1, devices_number=4, operation=VpnSubscriptionOffer.OperationType.GREATER_THAN_OR_EQUAL, discount_percentage=30),

        VpnSubscriptionOffer(month_duration=6, devices_number=1, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=0),
        VpnSubscriptionOffer(month_duration=6, devices_number=2, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=20),
        VpnSubscriptionOffer(month_duration=6, devices_number=3, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=25),
        VpnSubscriptionOffer(month_duration=6, devices_number=4, operation=VpnSubscriptionOffer.OperationType.GREATER_THAN_OR_EQUAL, discount_percentage=35),

        VpnSubscriptionOffer(month_duration=12, devices_number=1, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=0),
        VpnSubscriptionOffer(month_duration=12, devices_number=2, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=25),
        VpnSubscriptionOffer(month_duration=12, devices_number=3, operation=VpnSubscriptionOffer.OperationType.EQUAL, discount_percentage=30),
        VpnSubscriptionOffer(month_duration=12, devices_number=4, operation=VpnSubscriptionOffer.OperationType.GREATER_THAN_OR_EQUAL, discount_percentage=50)
    ])

    return Response(status=status.HTTP_201_CREATED)


class GetAllDurationPricesAPIView(generics.ListAPIView):
    model = VpnDurationPrice
    serializer_class = VpnDurationPriceSerializer
    queryset = VpnDurationPrice.objects.all()


class GetAllVpnSubscriptionOffersAPIView(generics.ListAPIView):
    model = VpnSubscriptionOffer
    serializer_class = VpnSubscriptionOffersSerializer
    queryset = VpnSubscriptionOffer.objects.filter().order_by('devices_number')


class GetAllVpnCountrySerializerAPIView(generics.ListAPIView):
    model = VpnCountry
    serializer_class = VpnCountrySerializer
    queryset = VpnCountry.objects.all()


class GetAllActiveVpnCountrySerializerAPIView(generics.ListAPIView):
    model = VpnCountry
    serializer_class = VpnCountrySerializer
    queryset = VpnCountry.objects.filter(instances__is_online=True)\
        .values('pkid', 'country', 'discount_percentage')\
        .annotate(dcount=Count('country'))


class GetActiveProtocolsAPIView(generics.ListAPIView):
    model = VpnProtocol
    serializer_class = VpnProtocolSerializer
    queryset = VpnProtocol.objects.filter(instances__is_online=True) \
        .values('pkid', 'protocol') \
        .annotate(dcount=Count('protocol'))

