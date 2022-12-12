from django.test import SimpleTestCase
from django.urls import resolve, reverse
from informasi.views import index

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.informasi_url = reverse('informasi:index')

    def test_qna_url_resolves(self):
        self.assertEqual(resolve(self.informasi_url).func, index)