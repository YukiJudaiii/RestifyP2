from django_filters import rest_framework as filters
from .models import Property, Reservation

class ReservationFilter(filters.FilterSet):
    user_type = filters.ChoiceFilter(choices=[('host', 'Host'), ('guest', 'Guest')], method='filter_user_type')
    state = filters.CharFilter(field_name='state', lookup_expr='iexact')

    class Meta:
        model = Reservation
        fields = fields = ['user_type', 'state']
        
    def filter_user_type(self, queryset, name, value):
        if value == 'host':
            return queryset.filter(property__owner=self.request.user)
        elif value == 'guest':
            return queryset.filter(user=self.request.user)
        else:
            return queryset
