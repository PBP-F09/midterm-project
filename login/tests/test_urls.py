from django.test import SimpleTestCase
from django.urls import resolve, reverse
from login.urls import registrasi_user, login_user, logout_user

class TestUrls(SimpleTestCase):
    def setUp(self):
        self.registrasi_url = reverse('login:registrasi_user')
        self.login_url = reverse('login:login_user')
        self.logout_user = reverse('login:logout_user')
    def test_registrasi_url_resolves(self):
        self.assertEqual(resolve(self.registrasi_url).func, registrasi_user)
    def test_login_url_resolves(self):
        self.assertEqual(resolve(self.login_url).func, login_user)
    def test_logout_url_resolves(self):
        self.assertEqual(resolve(self.logout_user).func, logout_user)
