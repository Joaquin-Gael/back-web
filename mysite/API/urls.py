from django.urls import (path, include)
from rest_framework import routers
from . import views
from users.urls import router as users_router
from posts.urls import router as posts_router

router = routers.DefaultRouter()

router.register(r'messages',views.MessagesAPI)
router.registry.extend(users_router.registry)
router.registry.extend(posts_router.registry)

urlpatterns = [
    path('users/',include('users.urls')),
    path('posts/',include('posts.urls')),
    path('web/',views.IndexAPI.as_view(),name='index'),
    path('',include(router.urls))
]
