from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.qna_html_url = reverse('qna:show_qna')
        self.qna_json_questions_url = reverse('qna:json_questions')
        self.qna_json_answers_url = reverse('qna:json_answers')
        self.qna_create_question= reverse('qna:create_question')
        self.qna_create_answer= reverse('qna:create_answer', args=[1])
        self.qna_delete_question= reverse('qna:delete_question', args=[1])
        self.qna_delete_answer= reverse('qna:delete_answer', args=[1])
        self.qna_like_question= reverse('qna:like_question', args=[1])

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

    def test_show_qna_create_question_resolves(self):
        response = self.client.get(self.qna_create_question)
        self.assertEqual(response.status_code, 302)

    def test_show_qna_create_answer_resolves(self):
        response = self.client.get(self.qna_create_answer)
        self.assertEqual(response.status_code, 302)

    def test_show_qna_delete_question_resolves(self):
        response = self.client.get(self.qna_delete_question)
        self.assertEqual(response.status_code, 302)

    def test_show_qna_delete_answer_resolves(self):
        response = self.client.get(self.qna_delete_answer)
        self.assertEqual(response.status_code, 302)

    def test_show_qna_like_question_resolves(self):
        response = self.client.get(self.qna_like_question)
        self.assertEqual(response.status_code, 302)
