import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from qna.models import *

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

        self.question = Question.objects.create(
            text="Anak saya batuk, kenapa ya?", 
            is_answered=False, 
            user= self.user, 
            date=datetime.date.today(), 
            role_user="bumil"
        )

        self.answer = Answer.objects.create(
            text="Radang tenggorokan", 
            user= self.user, 
            date=datetime.date.today(), 
            role_user="bumil",
            question=self.question,
        )
        
    
    def test_create_question(self):
        self.assertEqual(
            self.question, 
            Question.objects.get(user = self.user)
        )

    def test_create_answer(self):
        self.assertEqual(
            self.answer, 
            Answer.objects.get(user = self.user)
        )