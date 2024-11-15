from rest_framework import serializers
from .models import Comment, UserComment
from accounts.models import CustomUser
from rest_framework.fields import CurrentUserDefault
from accounts.serializers import UserSerializer
from django.core.validators import MinValueValidator, MaxValueValidator

class CommentReplySerializer(serializers.ModelSerializer):
    user = UserSerializer(default=CurrentUserDefault(), read_only=True)
    content = serializers.CharField(required=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at','parent_comment_id')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=CurrentUserDefault(), read_only=True)
    content = serializers.CharField(required=True)
    rate = serializers.IntegerField(required=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    parent_comment = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = CommentReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'property_id', 'content', 'rate', 'parent_comment', 'replies', 'created_at')


class UserCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(default=CurrentUserDefault(), read_only=True)
    target_username = serializers.CharField(write_only=True, required=True)
    content = serializers.CharField(required=True)
    rate = serializers.IntegerField(required=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        model = UserComment
        fields = ('id', 'author', 'target_username', 'content', 'rate' , 'created_at')

    def create(self, validated_data):
        target_username = validated_data.pop('target_username')
        target_user = CustomUser.objects.get(username=target_username)
        return UserComment.objects.create(target_user=target_user, **validated_data)



