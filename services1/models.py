from django.db import models

class Package(models.Model):
    
    """ model to add pacakges"""
    
    class Meta:
        verbose_name_plural = 'Package'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name

