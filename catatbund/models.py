from ast import mod
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class CatatbundModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight  = models.FloatField()
    height  = models.FloatField()
    bmi = 0

    def count_bmi(self):
        return self.weight / (self.height*self.height)
    
