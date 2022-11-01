from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.qna_html_url = reverse('qna:show_qna')
        self.qna_json_questions_url = reverse('qna:json_questions')
        self.qna_json_answers_url = reverse('qna:json_answers')

    def test_show_qna_html_resolves(self):
        response = self.client.get(self.qna_html_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'qna.html')

    def test_show_qna_json_questions_resolves(self):
        response = self.client.get(self.qna_json_questions_url)
        self.assertEqual(response.status_code, 200)

    def test_show_qna_json_answers_resolves(self):
        response = self.client.get(self.qna_json_answers_url)
        self.assertEqual(response.status_code, 200)
