from rest_framework.pagination import PageNumberPagination

class CommentsPageNumberPagination(PageNumberPagination):
    page_size = 2