
from django.urls import path
from . import views

urlpatterns = [
    path('new-chat/', views.NewChatView.as_view(), name='new-chat'),
]

