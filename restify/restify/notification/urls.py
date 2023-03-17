from django.urls import path
from .views import NotificationListView, NotificationReadView, NotificationClearView

urlpatterns = [
    path('view/', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', NotificationReadView.as_view(), name='notification-read'),
    path('<int:pk>/clear/', NotificationClearView.as_view(), name='notification-clear'),
]