from django.db.models import Q
from rest_framework import status

from apps.vpn_instance.models import VpnInstance


def get_available_instance(*, country_id, protocol_id) -> VpnInstance:
    query = Q(country__pkid=country_id, protocols__pkid=protocol_id, is_online=True)
    instances = VpnInstance.objects.filter(query)

    if len(instances) == 0:
        raise Exception('There are no available instances.')

    return instances[0]