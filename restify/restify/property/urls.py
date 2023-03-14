from django.urls import path
from .views import PropertyCreateAPIView, PropertyUpdateAPIView, PropertyListAPIView, PropertyDeleteAPIView

urlpatterns = [
    path('create/', PropertyCreateAPIView.as_view(), name='property_create'),
    path('update/<int:pk>/', PropertyUpdateAPIView.as_view(), name='property_update'),
    path('properties', PropertyListAPIView.as_view(), name='property_list'),
    path('delete/<int:pk>/', PropertyDeleteAPIView.as_view(), name='property_delete'),
]