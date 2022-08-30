from django.urls import path
from django.views.generic import TemplateView

from apps.metrics.views import collect_statistics

app_name = "metrics"

urlpatterns = [
    path('collect-metrics', collect_statistics)
]
