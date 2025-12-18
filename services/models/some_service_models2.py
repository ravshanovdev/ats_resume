from django.db import models
from .some_service_models import FirstInfoAnyService


class SuccessfullyDevelopment(models.Model):
    common_title = models.CharField(max_length=150)
    title_1 = models.CharField(max_length=250)
    description_1 = models.TextField()
    image_1 = models.ImageField(upload_to='images/', blank=True)
    title_2 = models.CharField(max_length=250, blank=True, null=True)
    description_2 = models.TextField(blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title_1



class ClientsOpinion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    grade = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} --> {self.description}"



class FrequentlyQuestion(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    first_info = models.ForeignKey(FirstInfoAnyService, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

