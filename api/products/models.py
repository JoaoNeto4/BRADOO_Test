from django.db import models
from pkg_resources import require
from vendors.models import Vendor


class Products(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    price = models.FloatField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.name