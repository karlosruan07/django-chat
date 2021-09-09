from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/home-content.html')

def login(request):
    return render(request, 'accounts/login-content.html')

def signup(request):
    return render(request, 'accounts/signup-content.html')