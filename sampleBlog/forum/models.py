from django.db import models

from core.models import User
# Create your models here.


class Category(models.Model):
    slug = models.SlugField(unique=True)
    category_name = models.CharField(max_length=255,)
    category_description = models.CharField(max_length=255,)


class SubCategory(models.Model):
    slug = models.SlugField(unique=True)
    subcategory_name = models.CharField(max_length=255,)
    subcategory_description = models.CharField(max_length=255, )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, null=True)


class Topic(models.Model):
    title = models.CharField(max_length=255,)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)

    def get_post_number(self):
        pass

    def get_page(self):
        pass

    def get_url(self):
        pass


class Post(models.Model):
    text = models.CharField(max_length=5000,)
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
