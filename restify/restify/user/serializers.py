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


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_repeat', 'first_name', 'last_name')

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


class ProfileSerializer(UserSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    confirm_new_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'new_password', 'confirm_new_password')

    def validate(self, data):
        if 'new_password' in data and 'confirm_new_password' in data:
            if data['new_password'] != data['confirm_new_password']:
                raise serializers.ValidationError("New passwords do not match.")
            data.pop('confirm_new_password')
        return super().validate(data)

    def update(self, instance, validated_data):
        if validated_data.get('email'):
            instance.email = validated_data['email']
        if validated_data.get('new_password'):
            instance.set_password(validated_data['new_password'])
        if validated_data.get('first_name'):
            instance.first_name = validated_data['first_name']
        if validated_data.get('last_name'):
            instance.last_name = validated_data['last_name']
        instance.save()
        return instance
