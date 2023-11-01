# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Django Views
from apps.blogs.views import PostListAPIView, PostDetailAPIView

# App name
app_name = 'blogs'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)