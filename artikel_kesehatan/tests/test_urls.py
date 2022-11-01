from django.test import SimpleTestCase
from django.urls import resolve, reverse
from artikel_kesehatan.views import show_artikel, show_artikel_by_id

class TestUrls(SimpleTestCase):
    def setUp(self):
        self.artikel_url = reverse('artikel_kesehatan:show_artikel')
        self.artikel_by_id_url = reverse('artikel_kesehatan:show_artikel_by_id', args=[1])
    def test_artikel_url_resolves(self):
        self.assertEqual(resolve(self.artikel_url).func, show_artikel)
    def test_artikel_by_id_url_resolves(self):
        self.assertEqual(resolve(self.artikel_by_id_url).func, show_artikel_by_id)