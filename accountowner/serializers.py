# from rest_framework.serializers import ModelSerializer
# from rest_framework import  serializers
# from .models import account
# # class AccountSerializers(ModelSerializer):
# #     email = serializers.CharField(source='user.email')
# #     password = serializers.CharField(source='user.password')
# #
# #     class Meta:
# #         model = account
# #         fields = (
# #             'email','password','mobile',
# #             'description','extra_charge',
# #             'vat','device_id','hotel_name',
# #
# #         )
# #
# #     def update(self, instance, validated_data):
# #         instance.email = validated_data.get('email',instance.email)
# #         instance.password = validated_data.get('password',instance.password)
# #         instance.mobile = validated_data.get('mobile',instance.mobile)
# #         instance.description = validated_data.get('description',instance.description)
# #         instance.extra_charge = validated_data.get('extra_charge',instance.extra_charge)
# #         instance.vat = validated_data.get('vat',instance.vat)
# #         instance.device_id = validated_data.get('device_id',instance.device_id)
# #         instance.hotel_name = validated_data.get('hotel_name',instance.hotel_name)
# #         instance.save()
# #         return instance
# #
# #
# #     def create(self, validated_data):
# #         return
#

from django.contrib.auth import update_session_auth_hash
from  rest_framework import  serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from .models import Account,AccountManager

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    confirm_password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = Account
        fields = (
            'email','mobile','password','confirm_password',
            'description','extra_charge','vat',
            'device_id','hotel_name',
        )

    def create(self, validated_data):
        return Account.object.create_user(**validated_data)
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        password = validated_data.get('password',None)
        confirm_password = validated_data.get('confirm_password',None)
        if password and password==confirm_password:
            instance.set_password(password)
        instance.description = validated_data.get('description',instance.description)
        instance.extra_charge = validated_data.get('extra_charge',instance.extra_charge)
        instance.vat = validated_data.get('vat',instance.vat)
        instance.device_id = validated_data.get('device_id',instance.device_id)
        instance.hotel_name = validated_data.get('hotel_name',instance.hotel_name)
        instance.save()
        return instance
    def validate(self, data):
        if data['password']:
            print('here')
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    'The password have to be same'
                )
        return data





# customJwtTokenSerializer


# from django.contrib.auth import authenticate
# class CustomJWTSerializer(JSONWebTokenSerializer):
#     username_field = 'mobile_or_email'
#     def validate(self, attrs):
#         password = attrs.get('password')
#         user_obj = Account.object.filter(email=attrs.get("mobile_or_email").first or Account.object.filter(mobile=attrs.get('mobile_or_email')))
#         if user_obj is not None:
#             credentials = {
#                 'mobile':user_obj.mobile,
#                 'password':password
#             }
#         if all(credentials.values()):
#             user = authenticate(**credentials)
#             if user:
#                 if not user.is_active: