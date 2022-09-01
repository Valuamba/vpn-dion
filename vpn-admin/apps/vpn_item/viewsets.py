import io
import logging
import os
from configparser import ConfigParser
from io import BytesIO

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from apps.vpn_item.models import VpnItem
from rest_framework.response import Response

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_vpn_item_info(request, vpn_item_id):
    logger.info(f'Get VPN Item {vpn_item_id} info')
    vpn_item = VpnItem.objects.get(pkid=vpn_item_id)
    return Response(data={
        'vpn_item_id': vpn_item.pkid,
        'country': vpn_item.instance.country.country,
        'protocol': vpn_item.protocol.protocol,
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_vpn_item_qrcode(request, device_id):
    vpn_item = VpnItem.objects.get(pkid=device_id)
    qrcode_b = vpn_item.generate_qrcode_bytes()
    return HttpResponse(qrcode_b.getvalue(), content_type="image/png")


@api_view(['GET'])
def get_vpn_config_file(request, vpn_item_id):
    logger.info(f'Get VPN config {vpn_item_id}')
    vpn_item = VpnItem.objects.get(pkid=vpn_item_id)
    config = vpn_item.get_config()

    with io.StringIO() as output:
        config.write(output)
        contents = output.getvalue()
        return HttpResponse(contents, content_type="text/plain")


@api_view(['GET'])
def get_subscription_vpn_items(request, subscription_id):
    logger.info(f'Get VPN Items of subscription {subscription_id}')
    vpn_items = VpnItem.objects.filter(vpn_subscription_id=subscription_id)

    data = []
    for vpn_item in vpn_items:
        data.append({
            'vpn_item_id': vpn_item.pkid,
            'country': vpn_item.instance.country.country,
            'protocol': vpn_item.protocol.protocol,
        })
    return Response(data=data, status=status.HTTP_200_OK)