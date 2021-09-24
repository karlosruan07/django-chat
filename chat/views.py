from django.shortcuts import render
from django.http import HttpResponse

def new_chat(request):
    return render(request, 'chat/new-chat.html')
