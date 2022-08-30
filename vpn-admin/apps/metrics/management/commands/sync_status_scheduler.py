import logging
import pprint
import subprocess
import time
from collections import namedtuple

import requests
from django.core.management import BaseCommand
from django.db import connections
from django.utils import timezone
from django.conf import settings
import time
from django.db.utils import DEFAULT_DB_ALIAS, load_backend
from apps.vpn_instance.models import VpnInstance
import threading

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def get_all_instances(self):
        connection = self.create_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM public.vpn_instances
                            ORDER BY pkid ASC 
                            """
                               )
                return self.namedtuplefetchall(cursor)
        except:
            raise
        finally:
            connection.close()

    def update_instance_state(self, is_online, instance_id, mac=None):
        connection = self.create_connection()
        try:
            if mac:
                with connection.cursor() as cursor:
                    query = "UPDATE public.vpn_instances SET is_online=%s, mac='%s' WHERE id='%s';" % (is_online, mac, instance_id)
                    cursor.execute(query)
            else:
                with connection.cursor() as cursor:
                    query = "UPDATE public.vpn_instances SET is_online=%s WHERE id='%s';" % (is_online, instance_id)
                    cursor.execute(query)
        except:
            raise
        finally:
            connection.close()

    def count_sync_threads(self):
        i = 0
        for thread in threading.enumerate():
            if thread.name.startswith("Sync_thread_"):
                print(f'Unclosed thread: {thread.name}')
                i += 1
        return i

    def create_connection(self, alias=DEFAULT_DB_ALIAS):
        connections.ensure_defaults(alias)
        connections.prepare_test_settings(alias)
        db = connections.databases[alias]
        backend = load_backend(db['ENGINE'])
        return backend.DatabaseWrapper(db, alias)

    def handle(self, *args, **kwargs):
        sem = threading.Semaphore()
        i = 0
        while True:
            print(f"Count of sync threads: {self.count_sync_threads()}")
            sem.acquire()
            try:
                instances = self.get_all_instances()
                for idx, instance in enumerate([*instances]):
                    thread_name = f"Sync_thread_{i}"
                    logger.info(f'Create thread {thread_name} for instance {instance.ip_address}:{instance.port}')
                    t = threading.Thread(target=self.sync_instance_state, args=[instance], daemon=True,
                                         name=thread_name
                                         )
                    t.start()
                    i += 1

                logger.info(f'Actual trade data: {threading.active_count()}')
                time.sleep(settings.SYNC_VPN_SERVER_INTERVAL_SECS)
            except Exception as e:
                logger.error(e)
                raise
            finally:
                sem.release()

    def sync_instance_state(self, instance):
        mac = None
        is_online = False
        try:
            response = requests.get(f'{instance.server_protocol}://{instance.ip_address}:{instance.port}/health', timeout=15)
            if response.status_code in [500, 502]:
                is_online = False
            elif response.json()['is_successful']:
                is_online = True
                conf_response = requests.get(f'http://{instance.ip_address}:{instance.port}/device-configuration',
                                             timeout=15
                                             )
                mac = conf_response.json()['MAC']
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            is_online = False
        logger.info(f'Instance {instance.name} is online.' if is_online else f'Instance {instance.name} is offline')
        self.update_instance_state(is_online, instance.id, mac)

    def namedtuplefetchall(self, cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('VpnInstance', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]
