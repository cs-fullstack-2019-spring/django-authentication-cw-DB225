from django.db import models


# Create your models here.
# username, calories and date
class FoodFitnessModel(models.Model):
    username = models.CharField(max_length=200)
    calories = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.username
