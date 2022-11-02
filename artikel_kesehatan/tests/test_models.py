import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from artikel_kesehatan.models import *

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()
        self.artikel = Artikel.objects.create(
            judul="Ini adalah judul artikel",
            isi="Ini adalah isi artikel",
            author= self.user,
            tanggal=datetime.date.today(),
        )
    def test_create_artikel(self):
        self.assertEqual(
            self.artikel, 
            Artikel.objects.get(author = self.user)
        )
        