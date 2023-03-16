from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LogInSerializer, ProfileSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


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


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username


class UserProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = ProfileSerializer
    
    def get_object(self, username):
        User = get_user_model()
        return get_object_or_404(User, username=username)
    
    def get(self, request, username):
        if request.user.username != username:
            # The user is not authorized to access this profile
            return Response({'error': 'You are not authorized to access this profile.'}, status=status.HTTP_403_FORBIDDEN)
        
        User = get_user_model()
        user = get_object_or_404(User, username=username)
        return Response({
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
    
    def put(self, request, username):
        user = self.get_object(username)
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
