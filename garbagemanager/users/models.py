from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('collector', 'Collector')])
