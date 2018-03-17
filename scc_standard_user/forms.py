# Django Imports
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# App Imports
from . models import StandardUser


# Auth Forms
class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password1 = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    password2 = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = StandardUser
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
