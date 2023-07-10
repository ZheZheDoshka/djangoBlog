from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View

from forum.models import *

# Create your views here.


class ForumView(View):
    """Main forum page. Lists all categories."""
    template_name = "forum/forum.html"
    def get(self, request):
        categories = list(Category.objects.order_by("category_position"))
        context = {'categories': categories}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


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
