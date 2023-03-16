from rest_framework import generics, permissions, serializers
from .models import Comment
from .serializers import CommentSerializer
from property.models import Property

class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        return Comment.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        property_id = self.request.data.get('property_id')
        try:
            property_instance = Property.objects.get(id=property_id)
            serializer.save(user=user, property=property_instance)
        except Property.DoesNotExist:
            raise serializers.ValidationError({"property_id": "Property with id " + property_id + "does not exist."})


class PropertyCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        property_id = self.kwargs['property_id']
        return Comment.objects.filter(property_id=property_id)

