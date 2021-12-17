from django.db import models


# Create your models here.
class Laptop(models.Model):
    company = models.CharField(max_length=32)
    model_name = models.CharField(max_length=32)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=50)
    price = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return self.company
