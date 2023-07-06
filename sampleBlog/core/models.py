from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = "User"
        ADMIN = "Administrator"
    # username = models.CharField(max_length=32)
    # email = models.EmailField()
    # password = models.CharField(max_length=64)

    role = models.CharField(
        max_length=15,
        choices=UserRole.choices,
        default=UserRole.USER
    )
