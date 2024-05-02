from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    template_name = 'accounts/logout.html'