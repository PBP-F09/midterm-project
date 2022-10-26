from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ROLE USER
class RoleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_faskes = models.BooleanField(default=False)
    is_bumil = models.BooleanField(default=False)