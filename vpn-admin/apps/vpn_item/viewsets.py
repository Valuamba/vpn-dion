from django.http import HttpResponse
from rest_framework.decorators import api_view
from apps.vpn_item.models import VpnItem


@api_view(['GET'])
def get_vpn_item_qrcode(request, device_id):
    vpn_item = VpnItem.objects.get(pkid=device_id)
    qrcode_b = vpn_item.generate_qrcode_bytes()
    return HttpResponse(qrcode_b.getvalue(), content_type="image/png")
