from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]