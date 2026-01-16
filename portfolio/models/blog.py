from django.db import models
from services.models.category_for_all_models import Category


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name






