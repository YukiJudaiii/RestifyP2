from django.shortcuts import render
from rest_framework import generics, status, permissions, mixins
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reservation
from property.models import Property
from .serializers import ReservationSerializer, ReservationActionSerializer
from .filters import ReservationFilter
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404


class ReservationPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ReservationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReservationFilter
    
# Reserve
class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        u = get_object_or_404(CustomUser, username=self.request.user.username)
        property_instance = self.request.data.get('property')
        property_name = Property.objects.get(id=property_instance).name
        serializer.save(user=self.request.user, state=Reservation.PENDING, property_name=property_name)

# Cancel
class ReservationCancelView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationActionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        reservation = self.get_object()
        u = get_object_or_404(CustomUser, username=self.request.user.username)
        if reservation.user == u:
            reservation.state = Reservation.CANCELED
            reservation.save()
        return self.update(request, *args, **kwargs)

# Approve/Deny Pending
class ReservationApproveDenyPendingView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationActionSerializer

    def perform_update(self, serializer):
        reservation = self.get_object()
        if reservation.property.owner == self.request.user:
            new_state = self.request.data.get('state')
            if new_state in [Reservation.APPROVED, Reservation.DENIED]:
                reservation.state = new_state
                reservation.save()

# Approve/Deny Cancel
class ReservationApproveDenyCancelView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationActionSerializer

    def perform_update(self, serializer):
        reservation = self.get_object()
        if reservation.property.owner == self.request.user:
            new_state = self.request.data.get('state')
            if new_state in [Reservation.APPROVED, Reservation.DENIED]:
                reservation.state = new_state
                reservation.save()

# Terminate
class ReservationTerminateView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationActionSerializer

    def perform_update(self, serializer):
        reservation = self.get_object()
        if reservation.property.owner == self.request.user:
            reservation.state = Reservation.TERMINATED
            reservation.save()