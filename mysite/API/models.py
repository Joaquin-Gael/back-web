from django.db import models

# Create your models here.
class MessagesAPI(models.Model):
    message = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)