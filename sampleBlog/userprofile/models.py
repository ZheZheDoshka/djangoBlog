from django.db import models
from core.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    profile_name = models.CharField(max_length=64, default="")
    description = models.CharField(max_length=255, default="")
    photo = models.ImageField(upload_to="images/user_profile",
                              default="images/user_profile/d1.png")