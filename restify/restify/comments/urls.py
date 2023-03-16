from django.urls import path
from django.contrib import admin

from .views import CommentsListAPIView, CommentsCreateAPIView

app_name = 'comments'

urlpatterns = [
    path('view/', CommentsListAPIView.as_view()),
    path('create/', CommentsCreateAPIView.as_view())
]