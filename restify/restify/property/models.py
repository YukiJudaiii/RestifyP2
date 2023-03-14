from django.db import models

# Create your models here.
class Property(models.Model):
    location = models.CharField(max_length=255)
    available_dates = models.CharField(max_length=255)
    guests = models.IntegerField()
    amenities = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
