from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.informasi_html_url = reverse('informasi:index')
        self.informasi_json_url = reverse('informasi:show_json')

    def test_show_informasi_html_resolves(self):
        response = self.client.get(self.informasi_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_show_informasi_json_resolves(self):
        response = self.client.get(self.informasi_json_url)
        self.assertEqual(response.status_code, 200)
