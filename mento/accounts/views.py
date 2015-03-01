from django.http import HttpResponseRedirect
from django.views.generic import (
    FormView, RedirectView, CreateView, TemplateView)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import (
        AuthenticationForm, SetPasswordForm, PasswordChangeForm)
from django.contrib.auth import (
    login as auth_login, logout as auth_logout, authenticate,
    update_session_auth_hash)

from braces.views import FormMessagesMixin, LoginRequiredMixin

from .mixins import NextUrlMixin
from .forms import UserCreateForm, PasswordRecoveryForm
from activities.models import Activity
from gear.models import Gear
from maintenance.forms import MaintenanceForm

from activities.tasks import get_strava_activities_by_user


class AccountRegistrationView(FormMessagesMixin, NextUrlMixin, CreateView):
    template_name = 'accounts/register.jinja'
    form_class = UserCreateForm
    success_url = reverse_lazy('dashboard')
    form_valid_message = 'Thank you for registering'
    form_invalid_message = 'Something went wrong. Please Try Again'

    def form_valid(self, form):
        saved_user = form.save()
        user = authenticate(
            username=saved_user.username,
            password=form.cleaned_data['password1'])
        auth_login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class NewAssociationView(TemplateView):
    template_name = 'accounts/new_association.jinja'

    def get(self, request, *args, **kwargs):
        get_strava_activities_by_user.delay(self.request.user.id)
        return super(NewAssociationView, self).get(request, args, kwargs)


class LoginView(FormMessagesMixin, NextUrlMixin, FormView):
    template_name = 'accounts/login.jinja'
    form_class = AuthenticationForm
    form_valid_message = 'You have successfully logged in.'
    form_invalid_message = 'Invalid Username or Password. Please Try Again'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, args, kwargs)


class PasswordRecoveryView(FormMessagesMixin, FormView):
    template_name = 'accounts/password_recovery.jinja'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('login')
    form_valid_message = 'Email has been sent with new login information'
    form_invalid_message = 'Email does not exist'

    def form_valid(self, form):
        form.reset_email()
        return super(PasswordRecoveryView, self).form_valid(form)


class SettingsView(LoginRequiredMixin, FormMessagesMixin, FormView):
    template_name = 'accounts/settings.jinja'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')
    form_valid_message = 'Password changed successfully'
    form_invalid_message = 'Error please try again'

    def get_form(self, form_class):
        return form_class(user=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(SettingsView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)

        context['strava'] = self.request.user.social_auth.filter(
            provider='strava').exists()
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.jinja'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        activities = Activity.objects.filter(
            user=self.request.user).order_by('-start_date')
        context['activities']  = activities
        context['gears'] = Gear.objects.filter(user=self.request.user)
        if activities.count() > 0:
            context['maintenance_form'] = MaintenanceForm(
                user=self.request.user)
        return context
