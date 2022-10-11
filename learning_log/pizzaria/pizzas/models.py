from sys import maxsize
from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete= models.CASCADE)
    igredients = models.CharField(max_length= 200)


    def __str__(self) -> str:
        return self.igredients