from django.db import models

class Order(models.Model):

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
        return self.full_name
    