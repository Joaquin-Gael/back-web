from django.urls import (path, include)
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViews, basename='users')
router.register(r'type_users', views.TypeUserViews, basename='type_users')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
