from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser

# Create your models here.
class Property(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner_first_name = models.CharField(max_length=255)
    owner_last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    available_dates = models.DateField()
    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    number_of_bedrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    number_of_washrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    contact_number = models.CharField(max_length=255)
    email = models.EmailField()
    amenities = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
