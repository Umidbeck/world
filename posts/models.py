from django.db import models

# Create your models here.
class PostModel(models.Model):
    text = models.TextField()