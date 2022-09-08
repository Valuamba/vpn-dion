import pprint

from django.core.management import BaseCommand
from django_countries.fields import Country

from apps.vpn_country.models import VpnCountry
from apps.vpn_instance.models import VpnInstance
from apps.vpn_protocol.models import VpnProtocol, VpnProtocolType
from django_countries import countries

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Notification.objects.exclude(pk__in=list(notes)).delete()


        wireguard = VpnProtocol.objects.get_or_create(protocol=VpnProtocolType.WIREGUARD)
        # open_vpn = VpnProtocol.objects.create(protocol=VpnProtocolType.OPEN_VPN)

        # print (f'Country: ${dict(countries)["BY"]}')

        # belarus = VpnCountry.objects.get_or_create(place='BY', discount_percentage=5, is_default=False)
        norway = VpnCountry.objects.get_or_create(place='NO', discount_percentage=20, is_default=True)
        # belgium = VpnCountry.objects.get_or_create(place='BO', discount_percentage=20, is_default=False)


        main_instance = VpnInstance.objects.create(ip_address='65.109.3.106', port=80, server_protocol=VpnInstance.HttpProtocol.HTTP, name="Main instance", country=norway[0], is_online=True)

        main_instance.protocols.add(wireguard[0])
        main_instance.save()