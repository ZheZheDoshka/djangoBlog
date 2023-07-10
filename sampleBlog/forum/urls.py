from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path("forum/", views.ForumView.as_view(), name='forum'),
    path("forum/<slug:category>/", views.CategoryView.as_view(), name='category'),
    path("forum/<slug:category>/<slug:subcategory>/", views.SubCategoryView.as_view(), name='subcategory'),
    path("forum/<slug:category>/<slug:subcategory>/<int:topic_id>/", views.TopicView.as_view(), name='topic'),
]
