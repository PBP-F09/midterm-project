from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ROLE USER
class RoleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = False
    is_faskes = False
    is_bumil = False