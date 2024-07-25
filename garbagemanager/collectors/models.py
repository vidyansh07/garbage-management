from django.db import models

# Create your models here
from django.db import models
from django.conf import settings

class Collector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collector_profile')
    employee_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Collector: {self.user.username}"