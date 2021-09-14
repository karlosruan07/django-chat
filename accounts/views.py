
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import User
from .forms import FormularioAdmin

from django.views import generic

def home(request):
    return render(request, 'accounts/home-content.html')


class SignupView(generic.CreateView):
    model = User
    template_name = 'accounts/signup-content.html'
    form_class = FormularioAdmin
    success_url = reverse_lazy('login')
