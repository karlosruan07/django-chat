from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login-content.html'
    ), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),

]