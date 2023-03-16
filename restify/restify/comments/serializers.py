from rest_framework import serializers
from .models import Comment
from rest_framework.fields import CurrentUserDefault
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=CurrentUserDefault(), read_only=True)
    property_id = serializers.IntegerField(write_only=True, required=True)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'property_id', 'content', 'created_at')

    