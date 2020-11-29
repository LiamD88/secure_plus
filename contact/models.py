from django.db import models
from django.utils import timezone

class Contact(models.Model):

    """ model to save contact form details"""

    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField(max_length=500)
 
    time = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name
    