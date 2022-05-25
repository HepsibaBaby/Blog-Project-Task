from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Profile(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")








