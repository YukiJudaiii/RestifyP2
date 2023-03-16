from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Property
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import filters, pagination
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied
from .filters import PropertyFilter


# Create your views here.

class PropertyCreateAPIView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
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
    
    def perform_update(self, serializer):
        property_instance = self.get_object()
        if self.request.user != property_instance.owner:
            raise PermissionDenied("You can only update your own properties.")
        serializer.save()
    
class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['location', 'from_date', 'to_date', 'guests', 'amenities']
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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PropertyFilter
    ordering_fields = ['price', 'guests']
    pagination_class = PropertyPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_queryset(queryset)
        return queryset