
from django.http import response
from django.test import TestCase
from accounts.models import User
from django.urls import reverse

class TestLogin(TestCase):
    
    def setUp(self):
        test_user1 = User.objects.create_user(username='user_teste', password='user_teste123')
        test_user1.save()

    def test_login_user(self):

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

        login = self.client.login(username='user_teste', password='user_teste123')
        response = self.client.get(reverse('home'))#acessa o view login e resgata o user autenticado
        self.assertEqual(str(response.context['user']), 'user_teste')
        self.assertEqual(response.status_code, 200)
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertEqual(response.status_code, 302)

    def test_template_access_home_if_logged(self):
        login = self.client.login(username='user_teste', password='user_teste123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home-content.html')

    def test_url_login(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)


class TestLogout(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='user_teste', password='user_teste123')
        test_user1.save()
    
    def test_logout(self):
        login = self.client.login(username='user_teste', password='user_teste123')
        response = self.client.get(reverse('home'))
        self.assertEqual(str(response.context['user']), 'user_teste')#verifica se está logado
    
        logout = self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        response = self.client.get('/accounts/logout/')
        self.assertRedirects(response, '/accounts/login/')
        self.assertEqual(response.status_code, 302)


class TestSignUp(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='user_teste', password='user_teste123')
        test_user1.save()

    def test_template_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup-content.html')

    def test_access_signup_user_not_logged_in(self):
        response = self.client.get(reverse('signup'))#acessa o view signup e resgata o user autenticado
        self.assertEqual(str(response.context['user']), 'AnonymousUser')
        self.assertEqual(response.status_code, 200)

    def test_url_signup(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
