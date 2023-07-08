from django.db import models
from core.models import User

# Create your models here.


class UserProfile(models.Model):
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    description = models.CharField(max_length=255,)
    # photo = models.ImageField()
