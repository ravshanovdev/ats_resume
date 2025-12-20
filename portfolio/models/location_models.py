from django.db import models


class Location(models.Model):
    zone = models.CharField(max_length=150, help_text='include zone or country')

    def __str__(self):
        return self.zone


class HelperLocation(models.Model):
    country = models.CharField(max_length=150, help_text='include country or region')
    description = models.TextField()
    location_url = models.URLField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.country


