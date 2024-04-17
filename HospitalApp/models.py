from django.db import models
from django.forms import forms


# Create your models here.

class mainpg(models.Model):
    def __str__(self):
        return self.mainpg

class Reg(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
