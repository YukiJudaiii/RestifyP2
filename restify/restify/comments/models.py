
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Comments(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    address_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    address_id = models.PositiveIntegerField()
    address_object = GenericForeignKey("address_type", "address_id")