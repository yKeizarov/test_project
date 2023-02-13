from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)


class MilitaryTech(models.Model):
    base_mark = models.CharField(max_length=20)
    full_mark = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    base_fuel_consumption = models.FloatField()
    special_fuel_consumption = models.FloatField()
    base_tank_volume = models.IntegerField()
    special_tank_volume = models.IntegerField()
    brand_motor_oil = models.CharField(max_length=20)
