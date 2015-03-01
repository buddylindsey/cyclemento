from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.jinja'), name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^maintenance/',
        include('maintenance.urls', namespace='maintenance')),
    url(r'^admin/', include(admin.site.urls)),
)
