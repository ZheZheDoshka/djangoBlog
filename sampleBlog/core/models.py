from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Slightly redefined User model. Might be redundant."""
    class UserRole(models.TextChoices):
        USER = "User"
        ADMIN = "Administrator"
        MODERATOR = "Moderator"
    # username = models.CharField(max_length=32)
    # email = models.EmailField()
    # password = models.CharField(max_length=64)

    role = models.CharField(
        max_length=15,
        choices=UserRole.choices,
        default=UserRole.USER
    )
    blocked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

