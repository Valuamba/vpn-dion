from django.urls import path

from notifications.viewsets import add_job

urlpatterns = [
    path('add-job', add_job)
]