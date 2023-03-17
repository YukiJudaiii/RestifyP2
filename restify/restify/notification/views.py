from rest_framework import generics, permissions, status
from .models import Notification
from .serializers import NotificationSerializer
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class NotificationPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = NotificationPagination

    def get_queryset(self):
        u = get_object_or_404(CustomUser, username=self.request.user.username)
        return Notification.objects.filter(recipient=u)

class NotificationReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        u = get_object_or_404(CustomUser, username=self.request.user.username)
        return Notification.objects.filter(recipient=u)
    
    def perform_update(self, serializer):
        instance = self.get_object()
        # u = get_object_or_404(CustomUser, username=self.request.user.username)

        instance.is_read = True
        instance.save()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationClearView(generics.DestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user)