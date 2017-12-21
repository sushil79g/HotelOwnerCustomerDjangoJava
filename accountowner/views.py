from django.shortcuts import render
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import AccountSerializer
from django.contrib.auth import login,authenticate
from .models import Account

# Create your views here.


class AuthRegister(APIView):
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AuthLogin(APIView):
    def post(self,request,format=None):
        data = request.data
        email = data.get('email',None)
        password = data.get('password',None)
        account = authenticate(email=email,password=password)
        if account is not None:
            login(request, account)
            return Response({
                'status':'Successful',
                'message':'You have successfully been logged into your account'
            }, status=status.HTTP_200_OK)
        return  Response({
            'status':'Unathorized',
            'message':'Username/password combination invalid.'
        },status= status.HTTP_401_UNAUTHORIZED )