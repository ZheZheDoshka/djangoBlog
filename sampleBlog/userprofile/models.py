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

    # photo = models.ImageField(upload_to="images/user_profile/%s" % (user.username()), height_field=64, width_field=64, ) #default=)
