from django.urls import path
from django.contrib import admin

from .views import (
    NotificationsCreateAPI,
    NotificationListAPIView,
    NotificationsDeleteAPIView,
    NotificationsDetailAPIView
)

app_name = 'notifications'

urlpatterns = [
    path('view/', NotificationListAPIView.as_view()),
    path('create/', NotificationsCreateAPI.as_view()),
    path('delete/', NotificationsDeleteAPIView.as_view()),
    path('<receiver_id>/', NotificationsDetailAPIView.as_view())
]