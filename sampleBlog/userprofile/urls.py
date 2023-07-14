from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path("profile/<str:profile_name>/", views.UserProfileView.as_view(), name='userprofile'),
]
