from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from diarybund.models import DiaryBund
import datetime

# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.diary = DiaryBund.objects.create(
            title="Anak saya hari ini sedih", 
            emotion=1, 
            user=self.user, 
            date=datetime.date.today(), 
            abstract="Sedih karena temannya sakit",
            description="Anak saya hari ini seidh karena temannya sakit demam berdarah"
        )
        self.client = Client()
        self.diarybund_html = reverse('diarybund:show_diarybund')
        self.diarybund_json = reverse('diarybund:show_json')

    def test_show_diarybund_html_resolves(self):
        response = self.client.get(self.diarybund_html)
        self.assertEqual(response.status_code, 302)

    def test_show_diarybund_json_resolves(self):
        response = self.client.get(self.diarybund_json)
        self.assertEqual(response.status_code, 302)