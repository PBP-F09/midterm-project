from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class DiaryBund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=200)
    emotion = models.IntegerField()
    abstract = models.CharField(max_length=200)
    description = models.TextField()