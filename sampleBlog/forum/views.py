from django.shortcuts import render, redirect, get_object_or_404
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
    template_name = "forum/category.html"

    def get(self, request, category):
        category = get_object_or_404(Category, slug=category)
        subcategories = list(SubCategory.objects.filter(category=category).order_by("subcategory_position"))
        context = {'subcategories': subcategories, 'category': category.category_name}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class SubCategoryView(View):
    template_name = "forum/subcategory.html"

    def get(self, request, category, subcategory):
        category = get_object_or_404(Category, slug=category)
        subcategory = get_object_or_404(SubCategory, slug=subcategory)
        topics = list(Topic.objects.filter(subcategory=subcategory).order_by("subcategory_position"))
        context = {'subcategory': subcategory, 'category': category.category_name,
                   'topics': topics}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class TopicView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
