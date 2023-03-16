from django.urls import path
from .views import ReservationViewSet, ReservationCreateView, ReservationCancelView, ReservationApproveDenyPendingView, ReservationApproveDenyCancelView, ReservationTerminateView

urlpatterns = [
    path('', ReservationViewSet.as_view({'get': 'list'}), name='list'),
    path('reserve/', ReservationCreateView.as_view(), name='reserve'),
    path('cancel/<int:pk>/', ReservationCancelView.as_view(), name='cancel'),
    path('approve-deny-pending/<int:pk>/', ReservationApproveDenyPendingView.as_view(), name='approve_deny_pending'),
    path('approve-deny-cancel/<int:pk>/', ReservationApproveDenyCancelView.as_view(), name='approve_deny_cancel'),
    path('terminate/<int:pk>/', ReservationTerminateView.as_view(), name='terminate'),
]