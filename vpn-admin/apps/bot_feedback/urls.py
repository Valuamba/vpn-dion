from django.urls import path

from apps.bot_feedback.views import add_feedback_message

urlpatterns = [
    path('message', add_feedback_message)
]