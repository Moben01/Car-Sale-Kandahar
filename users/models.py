# models.py
from django.db import models
from django.contrib.auth.models import User

class UserPhone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phones')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"