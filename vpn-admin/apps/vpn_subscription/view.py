import ast

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.vpn_item.serializers import VpnItemCreateSerializer
from apps.vpn_subscription.serializers import VpnSubscriptionSerializer


@api_view(['POST'])
def create_subscription(request):
    data = request.data
    vpn_items = [ast.literal_eval(item) for item in data.pop('vpn_items')]

    serializer = VpnSubscriptionSerializer(data)
    serializer.is_valid(True)
    serializer.save()

    new_vpn_items = []
    for vpn_item in vpn_items:
        new_vpn_item = VpnItemCreateSerializer().create({
            **vpn_item,
            'vpn_subscription_id': serializer.data.pkid
        }
        )
        new_vpn_items.append(new_vpn_item.id)

    return Response()