from django.db import models


class Post(models.Model):
    text = models.TextField(max_length=100)
