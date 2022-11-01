from django.db import models

# Create your models here.
class Note (models.Model):
    lokasi = models.CharField(max_length=32, blank=True, default='')
    tanggal = models.DateField(default='')
    waktu = models.CharField(max_length=32, default='')
    kapasitas_balita = models.IntegerField(default='')

    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-uploaded",)