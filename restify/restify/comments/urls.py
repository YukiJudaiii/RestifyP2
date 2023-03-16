from django.urls import path
from django.contrib import admin

from .views import PropertyCommentsView, CommentCreateView

app_name = 'comments'

urlpatterns = [
    path('view/', PropertyCommentsView.as_view()),
    path('commentProperty', CommentCreateView.as_view())
]