from django.db import models

class FirstInfoAnyService(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title



class SpecialData(models.Model):
    title_1 = models.CharField(max_length=250)
    description_1 = models.TextField()
    title_2 = models.CharField(max_length=250, blank=True, null=True)
    description_2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title_1


class UsedTechnologyAndOthers(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    first_info = models.ForeignKey(FirstInfoAnyService, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







