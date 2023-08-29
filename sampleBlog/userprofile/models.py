import os

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

    def update_photo(self, photo):
        old_photo = self.photo.path
        if "images/user_profile/d1.png" in old_photo:
            self.update(photo=photo)
        if os.path.exists(old_photo):
            os.remove(old_photo)
        self.update(photo=photo)

    def update_description(self, description):
        self.update(photo=description)

