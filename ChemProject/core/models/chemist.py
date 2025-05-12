from django.contrib.auth.models import AbstractUser
from django.db import models


class Chemist(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username
