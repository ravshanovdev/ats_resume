from django.db import models


class Statistic(models.Model):
    name = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Obyekt ID-si: {self.id}. <----> yaratilgan vaqt: {str(self.created_at)}"


class HelperStatistic(models.Model):
    count = models.IntegerField(default=0)
    description = models.TextField()
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE, related_name='helperstatistic')

    def __str__(self):
        return f"{self.count}"






