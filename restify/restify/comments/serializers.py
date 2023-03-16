from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer
from .models import Comments
from notification.serializers import NotificationsDetailSerializer


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'author',
            'content',
            'address_type',
            'address_id'
        ]


class CommentsSerializerCreate(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'content',
            'address_type',
            'address_id'
        ]

    # def create(self, validated_data):
    #     Notifications.objects.create(sender_type=get_user_model(),
    #                                  sender_id=self.context.get('request').user,
    #                                  receiver_id=validated_data["address_id"],
    #                                  reservation=False,
    #                                  cancellation=False,
    #                                  comment=True
    #                                  )
    #     return super().create(validated_data)

    def create(self, serializer):
        comment = serializer.save()
        notification_serializer = models.NotificationsDetailSerializer(data={
            'sender_type': ContentType.objects.get_for_model(comment.sender),
            'sender_id': comment.sender.pk,
            'receiver_id': comment.receiver.pk,
            'reservation': False,
            'cancellation': False,
            'comment': True,
            'content': f"{comment.sender.username} commented on your post: {comment.content}"
        })
        notification_serializer.is_valid(raise_exception=True)
        notification_serializer.save()
