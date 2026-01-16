from django.db import models
from services.models.category_for_all_models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    play_market_url = models.URLField()
    app_store_url = models.URLField()

    def __str__(self):
        return self.name


class UserOpinionAboutProduct(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    opinion = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"