import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from diarybund.models import DiaryBund

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

        self.diary = DiaryBund.objects.create(
            title="Anak saya hari ini sedih", 
            emotion=1, 
            user= self.user, 
            date=datetime.datetime.now(), 
            abstract="Sedih karena temannya sakit",
            description="Anak saya hari ini seidh karena temannya sakit demam berdarah"
        )        
    
    def test_create_question(self):
        self.assertEqual(
            self.diary, 
            DiaryBund.objects.get(user = self.user)
        )