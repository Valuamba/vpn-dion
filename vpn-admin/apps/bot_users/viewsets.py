from rest_framework.viewsets import ModelViewSet

from apps.bot_users.models import BotUser
from apps.bot_users.serializers import BotUserSerializer


class BotUserViewSet(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
