from django.contrib import admin

from forum.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_description", "category_position"]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["subcategory_name", "subcategory_description", "subcategory_position"]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Topic)  # temp
