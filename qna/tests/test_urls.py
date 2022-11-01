from django.test import SimpleTestCase
from django.urls import resolve, reverse
from qna.views import show_qna

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.qna_url = reverse('qna:show_qna')

    def test_qna_url_resolves(self):
        self.assertEqual(resolve(self.qna_url).func, show_qna)