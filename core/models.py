from django.db import models

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=10)
    table_code = models.CharField(max_length=4)

class Plate(models.Model):
    bill= models.ForeignKey(Bill, related_name='plates', on_delete=models.CASCADE)
    order = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.IntegerField()

    class Meta:
        unique_together = ['bill' , 'order']
        ordering = ['order']

        def __str__(self):
            return '%d: %s' % (self.order, self.name)