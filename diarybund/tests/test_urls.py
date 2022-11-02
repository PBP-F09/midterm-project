from django.test import SimpleTestCase
from django.urls import resolve, reverse
from diarybund.views import show_diarybund

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.diarybund_url = reverse('diarybund:show_diarybund')

    def test_diarybund_url_resolves(self):
        self.assertEqual(resolve(self.diarybund_url).func, show_diarybund)