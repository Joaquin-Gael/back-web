from django.urls import (path, include)
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViews, basename='users')
router.register(r'type_users', views.TypeUserViews, basename='type_users')

urlpatterns = [
    path('', include(router.urls), name='user_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('visit/', views.VisitCreateView.as_view(), name='visit_create'),
    path('visit/chart',views.VisitDataChart.as_view(),name='visit_chart'),
    path('token/user/id/', views.UserIDByToken.as_view(), name='user_id'),
]
