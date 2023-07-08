from django.db import models

from core.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255,)


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=255,)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, null=True)


class Topic(models.Model):
    topic_name = models.CharField(max_length=255,)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)


class Post(models.Model):
    text = models.CharField(max_length=255,)
    user = models.ForeignKey(Topic,
                             on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)