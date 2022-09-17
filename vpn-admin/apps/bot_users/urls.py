from django.urls import path

from apps.bot_users.views import create_user, \
    get_referral_data, update_user, user_list_ids, get_user_by_id, BotUsersActiveList

app_name ="bot_users"

urlpatterns = [
    path('active/', BotUsersActiveList.as_view(), name="get_active_users"),
    path('<str:user_id>/', get_user_by_id, name="get_bot_user"),
    path('create', create_user, name="create_bot_user"),
    path('update/<str:user_id>/', update_user, name="update_bot_user"),
    path('all', user_list_ids, name="get_all_bot_user"),
    path('referral/<str:user_id>', get_referral_data, name="get_referral_data")
]