from django.urls import path

from apps.bot_users.views import GetBotUserAPIView, UpdateBotUserAPIView, CreateBotUserAPIView, create_user, \
    GetAllUsersAPIView, get_referral_data, update_user

app_name ="bot_users"

urlpatterns = [
    path('<str:user_id>/', GetBotUserAPIView.as_view(), name="get_bot_user"),
    path('create', create_user, name="create_bot_user"),
    path('update/<str:user_id>/', update_user, name="update_bot_user"),
    path('all', GetAllUsersAPIView.as_view(), name="get_all_bot_user"),
    path('referral/<str:user_id>', get_referral_data, name="get_referral_data")
]