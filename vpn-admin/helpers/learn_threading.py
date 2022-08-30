import os
import random
import threading
from collections import namedtuple

import requests
from django.conf import settings
import time

from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vpn-admin.settings.development')

import django
django.setup()

from apps.vpn_instance.models import VpnInstance


def sync_instance_state(instance, cursor, idx):
    try:
        response = requests.get(f'http://{instance.ip_address}', timeout=30)
        if response.status_code == 500:
            is_online = False
        else:
            is_online = True
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        is_online = False
    # print (f'Handler for idx {idx}')
    # print(f'Online state of server {instance.ip_address} is {instance.is_online}')
    query="UPDATE public.vpn_instance_vpninstance SET is_online=%s WHERE id='%s';" % (is_online, instance.id)
    print (query)
    # cursor.execute(query)


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('VpnInstance', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


if __name__ == '__main__':
    i = 0

    with connection.cursor() as cursor:
        while True:
            cursor.execute("""
                        SELECT * FROM public.vpn_instance_vpninstance
                        ORDER BY pkid ASC 
                            """)
            for idx, instance in enumerate(namedtuplefetchall(cursor)):
                thread_name = f"Sync_thread_{i}"
                print(f'Create thread {thread_name} for instance {instance.ip_address}')
                t = threading.Thread(target=sync_instance_state, args=[instance, cursor, idx], daemon=True,
                                     name=thread_name)
                t.start()
                i += 1

            print(f'Actual trade data: {threading.active_count()}')
            time.sleep(30)

