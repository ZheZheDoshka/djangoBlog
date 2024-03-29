from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View

from core.models import User
from forum.models import *
from forum.forms import *


# Views for forum app


class ForumView(View):
    """View for main forum page. Lists all categories."""
    template_name = "forum/forum.html"

    def get(self, request):
        categories = list(Category.objects.order_by("category_position"))
        context = {'categories': categories}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class CategoryView(View):
    """View for category page. Lists all subcategories within category."""
    template_name = "forum/category.html"

    def get(self, request, category):
        category = get_object_or_404(Category, slug=category)
        subcategories = list(SubCategory.objects.filter(category=category).order_by("subcategory_position"))
        # last_posts = [subcategories[i].get_last_post() for i in range(len(subcategories))]
        context = {'subcategories': subcategories, 'category': category.category_name, }  # 'last_posts': last_posts}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class SubCategoryView(View):
    """View for subcategory page. Lists all topics within subcategory."""
    template_name = "forum/subcategory.html"

    def get(self, request, category, subcategory):
        url = u'forum/%s/%s/new' % (category, subcategory)
        category = get_object_or_404(Category, slug=category)
        subcategory = get_object_or_404(SubCategory, slug=subcategory)
        topics = list(Topic.objects.filter(subcategory=subcategory))  # .order_by("subcategory_position"))
        context = {'subcategory': subcategory, 'category': category.category_name,
                   'topics': topics, 'url': url}
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class TopicView(View):
    """View for topic page. Lists all posts within topic."""
    template_name = "forum/topic.html"

    def get(self, request, category, subcategory, topic_id):
        url = u'forum/%s/%s/%s' % (category, subcategory, topic_id)
        topic = get_object_or_404(Topic, id=int(topic_id))
        posts = list(Post.objects.filter(topic=topic).order_by("creation_date"))
        context = {'topic': topic,
                   'posts': posts, 'url': url}
        return render(request, self.template_name, context)

    def post(self, request, category, subcategory, topic_id):
        if request.POST["post_id"] != "none":
            post_id = request.POST['post_id']
            Post.objects.filter(id=post_id).delete()
            return redirect(request.get_full_path())
        text = request.POST['text']
        topic = get_object_or_404(Topic, id=int(topic_id))
        user = User.objects.get(username=request.user.username)
        Post(text=text, topic=topic, user=user).save()
        return redirect(request.get_full_path())


class NewTopic(View):
    """Topic form"""
    template_name = 'forum/create_topic.html'

    def get(self, request, category, subcategory):
        if request.user.is_authenticated:
            form = TopicForm()
            context = {'form': form, 'category': category, 'subcategory': subcategory}
            return render(request, self.template_name, context)
        return redirect("/forum/")

    def post(self, request, category, subcategory):
        title = request.POST['title']
        text = request.POST['text']
        subcategory_ = SubCategory.objects.get(slug=subcategory)
        user = User.objects.get(username=request.user.username)
        Topic(title=title, text=text, subcategory=subcategory_, user=user).save()
        return redirect(u'/forum/%s/%s' % (category, subcategory))
