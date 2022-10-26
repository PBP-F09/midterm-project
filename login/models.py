from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# ROLE USER
class MyUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_faskes = models.BooleanField(default=False)
    is_bumil = models.BooleanField(default=False)
    
