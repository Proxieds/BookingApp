from enum import unique
from django.db import models
from rest_framework.generics import GenericAPIView

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=13, unique=True)
    details = models.CharField(max_length=300)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.FloatField()