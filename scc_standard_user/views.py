# Django Imports
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView

# App Imports
from . import forms


# Views
# class Register(CreateView):
#     template_name = 'scc_standard_user/register.html'
#     form_class = forms.RegistrationForm
#     success_url = settings.LOGIN_REDIRECT_URL
class Register(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<p>Registration Not Available At This Time.</p>")

class Login(LoginView):
    authentication_form = forms.LoginForm
    template_name = 'scc_standard_user/login.html'


class Logout(LogoutView):
    next_page = settings.LOGIN_URL

