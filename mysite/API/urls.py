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
    path('web/',views.IndexAPI.as_view(),name='index'),
    path('',include(router.urls)),
    path('',include('users.urls')),
    path('login/',views.LoginAPI.as_view(),name='login'),
    path('logout/',views.LogoutAPI.as_view(),name='logout'),
    path('usersAPI/list/',views.UsersAPI.as_view(),name='users'),
]
