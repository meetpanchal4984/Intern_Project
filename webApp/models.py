from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(models.Model):
    Fristname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class SaveProduct(models.Model):
    Product_Name = models.CharField(max_length=50)
    Product_Image = models.ImageField(upload_to="image/")
    Product_Price = models.IntegerField(default=1,validators=[ MaxValueValidator(100),MinValueValidator(1)])

    def __str__(self):
        return self.Product_Name

