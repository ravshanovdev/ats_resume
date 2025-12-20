from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TeamMembers(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name






