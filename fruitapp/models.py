from django.db import models

# Create your models here.

class ActiveF(models.Manager):
    def get_queryset(self):     # overwrite get_querysetmethod  # own query set method defined 
        return super().get_queryset().filter(is_delete=0)


class InactiveF(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=1)


class Fruit(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    is_available = models.BooleanField(default=False)
    is_delete = models.SmallIntegerField(default=0)
    available_fruits = ActiveF()            # Custom model maager object  
    not_available_fruits = InactiveF()
    objects = models.Manager()


    def __str__(self):
        return self.name

    class Meta:
        db_table = "fruit"




