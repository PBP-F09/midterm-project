from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.informasi_html_url = reverse('informasi:viewInformasi')
        self.informasi_htmlFaskes_url = reverse('informasi:index')
        self.informasi_json_url = reverse('informasi:show_json')
        self.informasi_edit_url = reverse('informasi:editInfos', args=[1])

    def test_view_informasi_html_resolves(self):
        response = self.client.get(self.informasi_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_informasi.html')

    def test_show_informasi_json_resolves(self):
        response = self.client.get(self.informasi_json_url)
        self.assertEqual(response.status_code, 200)
        # JSON always redirected, not rendered to a template

    def test_faskes_informasi_html_resolves(self):
        response = self.client.get(self.informasi_htmlFaskes_url)
        self.assertEqual(response.status_code, 302)
        # not rendered to a template

    def test_edit_informasi_html_resolves(self):
        response = self.client.get(self.informasi_edit_url)
        self.assertEqual(response.status_code, 200)
 

    
    
