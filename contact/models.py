from django.db import models
from django.utils import timezone

class Contact(models.Model):

    name = models.CharField(max_length=150)
    message = models.TextField()
    email = models.EmailField()
    time = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name
    