from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.


class CategoryView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class SubCategoryView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class TopicView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
