from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Bookings(models.Model):

    name_of_booking = models.CharField(max_length=30)
    price_of_booking = models.CharField(max_length=30)
    available = models.BooleanField()
    # image = models.ImageField()


