from django.db import models

# Create your models here.
from accounts.models import CustomUser
from property.models import Property

class Reservation(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    DENIED = 'Denied'
    CANCELED = 'Canceled'
    TERMINATED = 'Terminated'
    COMPELETED = 'Completed'
    EXPIRED = 'Expired'

    RESERVATION_STATES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
        (CANCELED, 'Canceled'),
        (TERMINATED, 'Terminated'),
        (COMPELETED, 'Completed'),
        (EXPIRED, 'Expired'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    state = models.CharField(max_length=10, choices=RESERVATION_STATES, default=PENDING)

