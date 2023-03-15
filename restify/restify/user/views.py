from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, LogInSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class UserSignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserLoginAPIView(APIView):
    serializer_class = LogInSerializer
    
    def get(self, request):
        return Response({'message': 'This is the login page.'})
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response = Response({'message': 'Login successful! Welcome ' + username + '!'})

            # Set the access and refresh token cookies
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)

            # Set the JWT authentication header
            jwt_token = str(refresh.access_token)
            response['Authorization'] = 'Bearer ' + jwt_token

            return response
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
    

class UserLogoutAPIView(APIView):
    serializer_class = LogInSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        try:
            # Get the refresh token from the request cookies
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({'message': 'User is already logged out.'})

            user = request.user
            username = user.username
            
            # Blacklist the refresh token

            token = RefreshToken(refresh_token)
            token.blacklist()

            # Clear the access and refresh token cookies
            response = Response({'message': 'User ' + username + 'is successfully logged out.'})
            response.delete_cookie('refresh_token')
            response.delete_cookie('access_token')
            return response

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Get the user object
        user = request.user
        
        # Get the user's information
        user_info = {
            'id': user.id,
            'username': user.username,
        }
        
        # Serialize the user data and return it in the response
        serializer = UserSerializer(user)
        data = {
            'user': user_info,
            'profile': serializer.data
        }
        return Response(data)

