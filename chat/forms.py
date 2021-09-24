
from django import forms
from django.db import models
from django.forms import fields

from chat.models import Chat

class FormChat(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [
            "sender",
            "recipient",
            "subject",
            "message"
        ]

