from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from django.contrib.auth.forms import AuthenticationForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

