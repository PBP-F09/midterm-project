from django.db import models

# Create your models here.
class Note (models.Model):
    lokasi = models.CharField(max_length=32, blank=True, default='')
    tanggal = models.CharField(max_length=32, default='')
    waktu = models.CharField(max_length=32, default='')
    kapasitas_balita = models.IntegerField(max_length=32, default='')

    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-uploaded",)