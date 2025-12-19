from django.db import models


class CommonStep(models.Model):
    common_title = models.CharField(max_length=150)

    def __str__(self):
        return self.common_title


class Step(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_file = models.ImageField(upload_to='images/', blank=True)
    steps = models.ForeignKey(CommonStep, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




