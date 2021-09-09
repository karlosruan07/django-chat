from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'accounts/home-content.html')

def Login(request):
    return render(request, 'accounts/login-content.html')

def Signup(request):
    return render(request, 'accounts/signup-content.html')