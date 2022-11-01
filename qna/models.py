from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_answered = models.BooleanField(default=False)
    date = models.DateField()
    total_like = models.IntegerField(default=0)
    total_answer = models.IntegerField(default=0)
    role_user = models.TextField(default='bumil')

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    role_user = models.TextField(default='bumil')