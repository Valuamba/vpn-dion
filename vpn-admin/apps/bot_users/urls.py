from django.urls import path

from apps.bot_users.views import GetBotUserAPIView, UpdateBotUserAPIView, CreateBotUserAPIView, create_user, \
    GetAllUsersAPIView

urlpatterns = [
    path('<str:user_id>/', GetBotUserAPIView.as_view(), name="get_bot_user"),
    path('create', CreateBotUserAPIView.as_view(), name="create_bot_user"),
    path('update/<str:user_id>/', UpdateBotUserAPIView.as_view(), name="update_bot_user"),
    path('all', GetAllUsersAPIView.as_view(), name="get_all_bot_user")
]