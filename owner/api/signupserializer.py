# from rest_framework.serializers import Serializer, ModelSerializer
# from rest_framework import serializers
# from owner.models import User
# from django.contrib.auth.models import User


# class SignupSerializer(ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = (
#             'username','email','password','description','extra_charge','vat',
#             'device_id','hotel_name','ssid','speciality',
#         )

#     def create(self, validated_data):
#         user = super(SignupSerializer,self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user