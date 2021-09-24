
from django.urls import path
from . import views

urlpatterns = [
    path('new-chat/', views.new_chat, name='new-chat'),
]

