from django.db import models


class CommonOpenPosition(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class HelperOpenPosition(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    common_op = models.ForeignKey(CommonOpenPosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



