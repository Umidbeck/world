from django.db import models
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "category"
        verbose_name_plural = "Categories"

class PostModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'images/', null = True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title