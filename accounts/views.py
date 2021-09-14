from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import User
from .forms import FormularioAdmin

from django.views import generic

def home(request):
    return render(request, 'accounts/home-content.html')

def login(request):
    return render(request, 'accounts/login-content.html')

class SignupView(generic.CreateView):
    model = User
    template_name = 'accounts/signup-content.html'
    form_class = FormularioAdmin
    success_url = reverse_lazy('login')
