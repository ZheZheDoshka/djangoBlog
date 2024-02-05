"""
URL configuration for sampleBlog project.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.views import index

urlpatterns = [
    path('', include('core.urls')),
    path('', include('forum.urls')),
    path('', include('userprofile.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
