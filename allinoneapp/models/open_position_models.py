from django.db import models
from services.models.category_for_all_models import Category


class CommonOpenPosition(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class HelperOpenPosition(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    common_op = models.ForeignKey(CommonOpenPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



