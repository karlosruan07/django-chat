from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy

from chat.models import Chat

class NewChatView(generic.CreateView):
    model = Chat
    template_name = 'chat/new-chat.html'
    fields = [
            "sender",
            "recipient",
            "subject",
            "message"
        ]
    success_url = reverse_lazy('home')
    
