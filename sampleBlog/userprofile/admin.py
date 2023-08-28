from django.contrib import admin
from userprofile.models import *

# Register your models here.


# class UserProfileAdmin(admin.ModelAdmin):
#    list_display = ["profile_name"]


# Register your models here.
admin.site.register(UserProfile) #, UserProfileAdmin)