from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.diarybund_html = reverse('diarybund:show_diarybund')
        self.diarybund_json = reverse('diarybund:show_json')

    def test_show_diarybund_html_resolves(self):
        response = self.client.get(self.diarybund_html)
        self.assertEqual(response.status_code, 302)

    def test_show_diarybund_json_resolves(self):
        response = self.client.get(self.diarybund_json)
        self.assertEqual(response.status_code, 302)