from django.db import models
from services.models.category_for_all_models import Category

class CommonStep(models.Model):
    common_title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.common_title


class Step(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_file = models.ImageField(upload_to='images/', blank=True)
    steps = models.ForeignKey(CommonStep, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




