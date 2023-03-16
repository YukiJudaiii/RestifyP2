from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CommentsSerializer, CommentsSerializerCreate
from .models import Comments
from .pagination import CommentsPageNumberPagination


class CommentsCreateAPIView(CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    pagination_class = CommentsPageNumberPagination



class CommentsListAPIView(ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    pagination_class = CommentsPageNumberPagination