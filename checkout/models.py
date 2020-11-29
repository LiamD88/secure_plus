from django.db import models
from services1.models import Package

class Order(models.Model):

    """ this is the model to create an order"""

    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    company_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30, blank=False)
    street_address1 = models.CharField(max_length=100, blank=False)
    street_address2 = models.CharField(max_length=100, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f'{self.full_name}' 
    



class OrderLineItem(models.Model):

    """ this will allow us to see specific orders in the admin area """

    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return f'{self.quantity} {self.package.name} {self.package.price}'
     

    