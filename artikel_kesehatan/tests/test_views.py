from django.test import TestCase, Client
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from artikel_kesehatan.models import Artikel

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.artikel = Artikel.objects.create(
            judul="Ini adalah judul artikel",
            isi="Ini adalah isi artikel",
            author= self.user,
            tanggal=datetime.date.today(),
        )
        self.client = Client()
        self.artikel_html_url = reverse('artikel_kesehatan:show_artikel')
        self.artikel_html_by_id_url = reverse('artikel_kesehatan:show_artikel_by_id', args=[1])
        self.artikel_json_url = reverse('artikel_kesehatan:show_artikel_json')
        self.artikel_json_by_id_url = reverse('artikel_kesehatan:show_artikel_json_by_id', args=[1])

    def test_show_artikel_html_resolves(self):
        response = self.client.get(self.artikel_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artikel.html')

    def test_show_artikel_html_by_id_resolves(self):
        response = self.client.get(self.artikel_html_by_id_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artikel_by_id.html')

    def test_show_artikel_json_resolves(self):
        response = self.client.get(self.artikel_json_url)
        self.assertEqual(response.status_code, 200)
        
    def test_show_artikel_json_by_id_resolves(self):
        response = self.client.get(self.artikel_json_by_id_url)
        self.assertEqual(response.status_code, 200)
