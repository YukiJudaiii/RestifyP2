from django.urls import path
from .views import PropertyCreateAPIView, PropertyUpdateAPIView, PropertyListAPIView, PropertyDeleteAPIView

urlpatterns = [
    path('properties/create/', PropertyCreateAPIView.as_view(), name='property_create'),
    path('properties/update/<int:pk>/', PropertyUpdateAPIView.as_view(), name='property_update'),
    path('properties/', PropertyListAPIView.as_view(), name='property_list'),
    path('properties/delete/<int:pk>/', PropertyDeleteAPIView.as_view(), name='property_delete'),
]