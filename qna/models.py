from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_answered = models.BooleanField(default=False)
    date = models.DateField()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)