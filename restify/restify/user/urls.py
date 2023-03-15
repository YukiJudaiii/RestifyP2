from django.urls import path
from .views import UserSignUpAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view(), name='user_signup'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
]