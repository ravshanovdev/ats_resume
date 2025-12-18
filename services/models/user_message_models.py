from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


BUDGET_CHOICE = (
    ('<$25.000', '$25.000'),
    ('$50.000', '$50.000'),
    ('$100.000', '$100.000'),
    ('$300.000', '$300.000')
)


class TellUsAboutYourProject(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    industry = models.CharField()
    budget = models.CharField(max_length=150, choices=BUDGET_CHOICE)

    def __str__(self):
        return f"{self.name} -- {self.phone}"

