from django.conf.urls import patterns, url, include

from .views import (
    AccountRegistrationView, LoginView, LogoutView, PasswordRecoveryView,
    DashboardView, SettingsView)

urlpatterns = patterns(
    '',
    url(r'^register/$', AccountRegistrationView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^password_recovery/$', PasswordRecoveryView.as_view(),
        name='password_recovery'),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^settings/$', SettingsView.as_view(), name="settings"),
)
