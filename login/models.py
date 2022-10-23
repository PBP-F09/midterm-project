from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ROLE USER
class RoleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Admin(RoleUser):
    def __init__(self, user):
        super().__init__(user)
        is_admin = True
class Faskes(RoleUser):
    def __init__(self, user):
        super().__init__(user)
        is_faskes = True
class Bumil(RoleUser):
    def __init__(self, user):
        super().__init__(user)
        is_bumil = True