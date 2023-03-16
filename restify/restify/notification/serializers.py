from rest_framework.serializers import ModelSerializer
from .models import Notifications


class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = [
            'sender_type',
            'sender_id',
            'receiver_id',
            'reservation',
            'cancellation',
            'comment'
        ]


class NotificationsDetailSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = [
            'sender_type',
            'sender_id',
            'receiver_id',
            'reservation',
            'cancellation',
            'comment',
            'content'
        ]