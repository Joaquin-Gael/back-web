from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.TypeUser)
admin.site.register(models.Visit)
admin.site.register(models.WeeklyVisit)