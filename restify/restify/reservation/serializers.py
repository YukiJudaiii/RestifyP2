from rest_framework import serializers
from .models import Reservation, Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'owner']

class ReservationSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'property', 'from_date', 'to_date', 'state']
        read_only_fields = ['user', 'state']

    def validate(self, data):
        if data['to_date'] <= data['from_date']:
            raise serializers.ValidationError("The 'to_date' must be later than the 'from_date'")
        
        property = data['property']
        
        if data['from_date'] < property.from_date or data['to_date'] > property.to_date:
            raise serializers.ValidationError("The reservation dates must be within the property's available dates.")

        
        duplicate_reservations = Reservation.objects.filter(
            property=data['property'],
            from_date__lte=data['to_date'],
            to_date__gte=data['from_date']
        )

        # also check if the reservation is already canceled or denied
        if duplicate_reservations.exists() and (not duplicate_reservations.filter(state=Reservation.CANCELED).exists() or not duplicate_reservations.filter(state=Reservation.DENIED).exists()):
            raise serializers.ValidationError("The property is already booked during the specified dates.")

        return data

class ReservationActionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'property', 'from_date', 'to_date', 'state']
        read_only_fields = ['id', 'user', 'property', 'from_date', 'to_date', 'state']