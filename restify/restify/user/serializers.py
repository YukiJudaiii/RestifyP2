from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    address = serializers.CharField(max_length=100, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_repeat', 'first_name', 'last_name', 'address', 'phone_number')

    def validate_password_length(self, value):
        """
        Check that the password has a length of at least 8 characters
        """
        if len(value) < 8:
            raise serializers.ValidationError("The password must be at least 8 characters long.")
        return value

    def validate_passwords(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError("Two pass words didn't match")
        return data
    
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        if validated_data.get('first_name'):
            user.first_name = validated_data['first_name']
        if validated_data.get('last_name'):
            user.last_name = validated_data['last_name']
        if validated_data.get('address'):
            user.address = validated_data['address']
        if validated_data.get('phone_number'):
            user.phone_number = validated_data['phone_number']
        user.save()
        return user


class LogInSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        data = super().validate(attrs)
        return data
