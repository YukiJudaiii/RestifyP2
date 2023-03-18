from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name', 'owner_first_name', 'owner_last_name', 'location', 'from_date', 'to_date', 'guests', 'number_of_bedrooms', 'number_of_washrooms', 'contact_number', 'email', 'amenities', 'price', 'image']