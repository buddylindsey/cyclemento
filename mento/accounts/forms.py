from django import forms
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .utils import generate_password


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField(required=False)

    def clean_email(self):
        try:
            return User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            raise forms.ValidationError("Can't find a user based on the email")
        return self.cleaned_data['email']

    def reset_email(self):
        user = self.cleaned_data['email']

        password = generate_password()
        user.set_password(password)
        user.save()
        body = """
 Sorry you are having issues with your account. Below is your username and
 new password:
 Username: {username}
 Password: {password}
 You can login here: http://cyclemento.com/accounts/login/
 Change your password here: http://cyclemento.com/accounts/settings/
 """.format(username=user.username, password=password)

        email = EmailMessage(
            '[CycleMento] Password Reset', body, 'no-reply@cyclemento.com',
            [user.email])
        email.send()
