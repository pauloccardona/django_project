from django.db import models

# Create your models here.
class Transaction(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

class Plate(models.Model):
    name = models.CharField(max_length=32)
    transactions = models.ManyToManyField(Transaction)

    def __str__(self):
        return self.name

class Extra(models.Model):
    name = models.CharField(max_length=16)
    plates = models.ManyToManyField(Plate)

    def __str__(self):
        return self.name