from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul