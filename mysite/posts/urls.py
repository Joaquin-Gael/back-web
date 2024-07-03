from django.urls import (path, include)
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'posts', views.PostsViews, basename='posts')
router.register(r'comments', views.CommentViews, basename='comments')
router.register(r'likes', views.LikeViews, basename='likes')
router.register(r'files', views.FilePostViews, basename='files')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/file/', views.PostsViews.as_view({'get':'get_file'}), name='file_post')
]
