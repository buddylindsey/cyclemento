from django.conf.urls import patterns, url, include

from .views import MaintenanceCreateView

urlpatterns = patterns(
    '',
    url(r'^add/$', MaintenanceCreateView.as_view(), name='add'),
)
