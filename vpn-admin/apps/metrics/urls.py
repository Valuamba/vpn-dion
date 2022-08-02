from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^admin/preferences/$', TemplateView.as_view(template_name='admin/preferences/preferences.html')),
    path('metrics/', TemplateView.as_view(template_name='admin/metrics/home.html'))
]