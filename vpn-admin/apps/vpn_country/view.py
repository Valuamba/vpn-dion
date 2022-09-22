from django.db.models import Q, Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from apps.vpn_country.models import VpnCountry


class VpnCountryList(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VpnCountry
            fields = [ 'discount_percentage', 'is_default', 'country', 'pkid', 'place', 'locale_ru' ]

    def get(self, request):
        query = Q(vpn_instances__is_online=True)
        countries = VpnCountry.objects.filter(query).order_by('locale_ru').annotate(total=Count('pkid'))

        serializer = self.OutputSerializer(countries, many=True)

        return Response(data=serializer.data)