from django.db import models

# Create your models here.
class MessagesAPI(models.Model):
    message = models.TextField()
    date = models.DateField(auto_now_add=True)