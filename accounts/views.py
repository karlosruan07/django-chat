
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .models import User
from .forms import FormularioAdmin

from django.views import generic

@login_required
def home(request):

    if request.user.is_authenticated:
        return render(request, 'accounts/home-content.html')
    else:
        return redirect('login')

class SignupView(generic.CreateView):
    model = User
    template_name = 'accounts/signup-content.html'
    form_class = FormularioAdmin
    success_url = reverse_lazy('login')
