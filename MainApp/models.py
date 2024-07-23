from django.db import models
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class Languages(models.Model):
    country = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
