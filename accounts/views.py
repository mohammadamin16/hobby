from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from films.forms import LoginForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')