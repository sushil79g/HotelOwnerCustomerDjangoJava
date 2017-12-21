# from django.shortcuts import render
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework import permissions
# from .serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.

# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def create_user(request):
#     serialized = UserSerializer(data=request.data)
#     if serialized.is_valid():
#         serialized.save()
#         return Response(serialized.data,status=status.HTTP_201_CREATED )
#     else:
#         return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, profileSerializer
from rest_framework import generics
from .models import Profile
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
# from rest_framework_jwt.views import obtain_jwt_token

User = get_user_model()
# class UserSignUp(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request, format=None):
#         query = User.objects.all()
#         serialize = UserSerializer(query, many=True)
#         return Response(serialize.data)

#     def post(self, request, format=None):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             username = serializer.data['username']
#             email = serializer.data['email']
#             password = serializer.data['password']
#             # User.objects.Create(['username'=username, 'email'=email, 'password'=password])
#             description = serializer.data['description']
#             extra_charge = serializer.data['extra_charge']
#             vat = serializer.data['vat']
#             device_id = serializer.data['device_id']
#             hotel_name = serializer.data['hotel_name']
#             # ssid = serializer.data['ssid']
#             # speciality = serializer.data['speciality']
#             user = User.objects.create_user(
#                 username = username,
#                 email = email,
#                 # description = description,
#                 # extra_charge = extra_charge,
#                 # vat = vat,
#                 # hotel_name = hotel_name,
#                 # ssid = ssid,
#                 # speciality = speciality
#             )
#             user.set_password(password)
#             user.save()
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

class UserListSignUp(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

# class UserUpdateSignUp(generics.UpdateAPIView):
#     pagination_class = [AllowAny]
#     queryset = UserProfile.objects.get('pk')
#     serializer_class =UserProfileSerializer

#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)

# class UserSignUp(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer