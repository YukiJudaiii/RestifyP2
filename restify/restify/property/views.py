from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Property
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.

class PropertyCreateAPIView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['location', 'available_dates', 'guests', 'amenities']
    ordering_fields = ['price', 'rating']
    pagination_class = LimitOffsetPagination
    
class PropertyDeleteAPIView(DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer