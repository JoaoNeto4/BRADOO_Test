from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    cnpj = models.CharField(max_length=11,  unique=True, null=False, blank=False)
    city = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.name
