from django.db import models

# Create your models here.
class Transaction(models.Model):
    code = models.CharField(max_length=10)

class Plate(models.Model):
    name = models.CharField(max_length=32)
    transactions = models.ManyToManyField(Transaction)

class Extra(models.Model):
    name = models.CharField(max_length=16)
    plates = models.ManyToManyField(Plate)