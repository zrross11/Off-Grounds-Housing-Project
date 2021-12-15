from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = '../login'
    template_name = 'registration/signup.html'
