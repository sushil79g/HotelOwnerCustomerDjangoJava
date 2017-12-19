# from rest_framework.views import APIView
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import permissions
# from .signupserializer import SignupSerializer
# from rest_framework.response import Response
# from rest_framework import status
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def create_user(request):
#     serialized = SignupSerializer(data=request.data)
#     if serialized.is_valid():
#         serialized.save()
#         return Response(serialized.data,status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)