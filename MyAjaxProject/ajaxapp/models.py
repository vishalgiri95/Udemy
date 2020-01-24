from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    pages = models.IntegerField()

