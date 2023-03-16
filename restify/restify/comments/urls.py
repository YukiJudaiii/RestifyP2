from django.urls import path
from django.contrib import admin

from .views import PropertyCommentsView, CommentCreateView, UserCommentsView

app_name = 'comments'

urlpatterns = [
    path('view/property/<int:property_id>', PropertyCommentsView.as_view()),
    path('commentProperty', CommentCreateView.as_view()),
    path('myComments', UserCommentsView.as_view()),
]