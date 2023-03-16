from rest_framework.pagination import PageNumberPagination


class NotificationsPageNumberPagination(PageNumberPagination):
    page_size = 2