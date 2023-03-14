from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Property
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import filters, pagination


# Create your views here.

class PropertyCreateAPIView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    def get(self, request, fomat=None):
        qs = Property.objects.all()
        serializer = PropertySerializer(qs, many=True)
        return Response(serializer.data)

class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # def get(self, request, fomat=None):
    #     qs = Property.objects.all()
    #     serializer = PropertySerializer(qs, many=True)
    #     return Response(serializer.data)
    
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

class PropertyPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class PropertySearchView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['location', 'amenities', 'available_dates', 'guests']
    ordering_fields = ['price', 'rating']
    filter_fields = ['location', 'amenities', 'available_dates', 'guests']
    pagination_class = PropertyPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_queryset(queryset)
        return queryset