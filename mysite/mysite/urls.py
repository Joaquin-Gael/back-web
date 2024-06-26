from django.contrib import admin
from django.urls import (path, include)
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('API.urls')),
    path('', lambda _:redirect(to='index'))
]
