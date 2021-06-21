from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    text = models.TextField(max_length=100)
