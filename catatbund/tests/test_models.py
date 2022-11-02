from django.test import TestCase
from django.contrib.auth.models import User
from catatbund.models import *
import datetime

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.catatbund = CatatbundModel.objects.create(
            user = self.user,
            date = '2022-11-12',
            weight  = 22,
            height  = 1.2,
            bmi = 22 / (1.2*1.2)
        )
    def test_create_artikel(self):
        self.assertEqual(
            self.catatbund, 
            CatatbundModel.objects.get(user = self.user)
        )
        