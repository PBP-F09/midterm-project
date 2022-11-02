import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from informasi.models import *

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

        self.informasi = Note.objects.create(
            user= self.user, 
            lokasi = "RS Hermina Jakarta Selatan",
            waktu = "10.00 - 12.00",
            kapasitas_balita = 2,
            tanggal = "2022-12-21",
        )

 

    
    def test_create_informasi(self):
        self.assertEqual(
            self.informasi, 
            Note.objects.get(user = self.user)
        )

