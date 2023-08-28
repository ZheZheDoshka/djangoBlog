import math

from django.db import models

from datetime import date

from core.models import User
# Create your models here.

POSTS_PER_PAGE = 10


class Category(models.Model):
    slug = models.SlugField(unique=True)
    category_name = models.CharField(max_length=255, default="")
    category_description = models.CharField(max_length=255, default="")
    category_position = models.IntegerField(default=10)

    def __unicode__(self):
        return self.category_name


class SubCategory(models.Model):
    slug = models.SlugField(unique=True)
    subcategory_name = models.CharField(max_length=255, default="")
    subcategory_description = models.CharField(max_length=255, default="")
    subcategory_position = models.IntegerField(default=10)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.subcategory_name


class Topic(models.Model):
    title = models.CharField(max_length=255, default="title")
    text = models.CharField(max_length=5000, default="")
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.title

    def get_post_number(self):
        return Post.objects.filter(topic=self).count()

    def get_page(self):
        return int(self.get_post_number()/POSTS_PER_PAGE)

    def get_url(self):
        return u'forum/%s/%s/%s?page=%s' % (self.subcategory.category.slug, self.subcategory.slug, self.id, self.get_page())

    def get_last_post(self):
        post = Post.objects.filter(topic=self).order_by('-creation_date')
        if post:
            return post[0]
        else:
            return self



class Post(models.Model):
    text = models.CharField(max_length=5000, default="")
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
