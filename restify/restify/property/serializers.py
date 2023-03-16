from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Property
        fields = ['owner_first_name', 'owner_last_name', 'location', 'available_dates', 'guests', 'number_of_bedrooms', 'number_of_washrooms', 'contact_number', 'email', 'amenities', 'price']