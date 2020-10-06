from django.db import models

class One(models.Model):
    
    class Meta:
        verbose_name_plural = 'One'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name

class Monthly(models.Model):

    class Meta:
        verbose_name_plural = 'Monthly'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name


class Yearly(models.Model):

    class Meta:
        verbose_name_plural = 'Yearly'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name