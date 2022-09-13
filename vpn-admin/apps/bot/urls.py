from django.urls import path

from apps.bot.views import BotUserUpdate, BotUserCreate, BotUserDetails, BotUserReferralDetails, MessageLocaleBulkList, \
    MessageLocaleRetrieve, FeedbackMessageCreate

urlpatterns = [
    path('message', FeedbackMessageCreate.as_view()),
    path('bulk-locale', MessageLocaleBulkList.as_view()),
    path('locale/<str:alias>', MessageLocaleRetrieve.as_view()),
    path('<str:user_id>/', BotUserDetails.as_view(), name="get_bot_user"),
    path('create', BotUserCreate.as_view(), name="create_bot_user"),
    path('update/<str:user_id>/', BotUserUpdate.as_view(), name="update_bot_user"),
    # path('all', user_list_ids, name="get_all_bot_user"),
    path('referral/<str:user_id>/', BotUserReferralDetails.as_view(), name="get_referral_data")
]