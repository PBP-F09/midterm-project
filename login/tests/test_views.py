from django.test import TestCase, Client
from django.urls import reverse
import datetime
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.client = Client()
        self.registrasi_html_url = reverse('login:registrasi_user')
        self.login_html_url = reverse('login:login_user')
        self.logout_url = reverse('login:logout_user')
    def test_registrasi_html_url_resolves(self):
        response = self.client.get(self.registrasi_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrasi.html')
    def test_login_html_url_resolves(self):
        response = self.client.get(self.login_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    def test_logout_url_resolves(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
