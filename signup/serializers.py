from rest_framework import serializers
from rest_framework.serializers import ModelSerializer 
from .models import UserProfile
# from .models import Ssidsignup,Specialitysignup
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
import hashlib, uuid

User = get_user_model()

# class SsidSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ssidsignup

# class SpecialitysignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Specialitysignup




class UserSerializer(ModelSerializer):
    # profile = profileSerializer()
    class Meta:
        model = User
        fields = [
            'email','password','username'
        ]
# class profileSerializer(ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = Profile
#         fields = [
#             'user','description', 'extra_charge',
#             'vat','device_id','hotel_name'

#         ]
#         # exclude = [
#         #     'id'
#         # ]










# class UserSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(label='Confirm_Password')
#     username = serializers.CharField(source='user.username',validators=[UniqueValidator(queryset=User.objects.all())])
#     password = serializers.CharField(source='user.password')
#     email = serializers.EmailField(source = 'user.email')
#     # description = serializers.CharField(source='description')
#     # extra_charge = serializers.BooleanField(source='extra_charge')
#     # vat = serializers.BooleanField(source='vat')
#     # ssid = SsidSerializer(many = True)
#     # speciality = SpecialitysignupSerializer(many=True)

#     class Meta:
#         model = Profile
#         fields=[
#             'username','email','password','password2','description','extra_charge',
#             'vat','device_id','hotel_name'
#             # ,'ssid','speciality'
#         ]

#     def validate(self, data):
#         # user = super(UserSerializer,self).create(validate_data)
#         # user.set_password(validate_data['password'])
#         # user.save()
#         # return user
#         pass1 = data.get('password')
#         pass2 = data.get('password2')
#         email = data.get('email')
#         user_email = Profile.objects.filter(email=email)
#         if pass1!=pass2:
#             raise ValidationError('Password ')
#         if user_email.exists():
#             raise ValidationError('User with email id:{} already exists'.format(email))
#         return data


    # def validate(self, data):
    #     pass1 = data.get('password1')
    #     pass2 = data.get('password2')
    #     if pass1 != pass2:
    #         raise ValidationError('password')
    #     return data



class UserProfileSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    # description = serializers.CharField('description')
    # extra_charge = serializers.BooleanField('extra_charge')
    # vat = serializers.BooleanField('vat')
    # hotel_name = serializers.CharField('hotel_name')
    
    class Meta:
        model = UserProfile
        fields = (
            'username','email','password','description',
            'extra_charge','vat','hotel_name','mobile'
        )

    def update(self ,instance, validate_data):
            instance.user.email = validate_data['user']['email']
            instance.user.password = validate_data['user']['password']
            instance.description = validate_data['description']
            instance.extra_charge= validate_data['extra_charge']
            instance.vat = validate_data['vat']
            instance.hotel_name = validate_data['hotel_name']
            instance.mobile = validate_data['mobile']
            instance.save()
            return instance

    def create(self, validate_data):
            # test = validate_data.get('user.password')
            # # salt = uuid.uuid4().hex
            # # hased_pass = hashlib.sha512(test + salt).hexdigest()
            # print('\n')
            # print(test)
            # print('\n')
            # passw = validate_data['user']['password']
            salt = uuid.uuid4().hex
            hashed = hashlib.sha512(validate_data['user']['password'].encode('utf-8') + salt.encode('utf-8')).hexdigest()
            # print(validate_data['user']['email'])
            
            # hashed = hashlib.sha512(validate_data['user']['password'] + salt).hexdigest()
            user = User.objects.create(username= validate_data['user']['username'],email= validate_data['user']['email'],password=hashed)
            return UserProfile(user=user)



    # user = User.objects.create(username= attrs.get('user.username'),email=attrs.get('user.email'),password=attrs.get('user.password'))
    #     return UserProfile(user=user)