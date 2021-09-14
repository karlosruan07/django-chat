
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import User
from django.db.models import fields

class FormularioAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']#A senha e a confirmação de senha o UserCreationForm já trata disso

