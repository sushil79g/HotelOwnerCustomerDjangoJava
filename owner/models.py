from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Signup(models.Model):
    username = models.CharField(max_length=256,default='')
    email = models.EmailField(unique=True, max_length=250)
    # password = models.CharField(max_length=50, validators=[RegexValidator(regex='^.{8}$', message='Minimum 8 character required!!!', code='nomatch')])
    # token = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=250, default='')
    extra_charge = models.BooleanField(default=False)
    vat = models.BooleanField(default=True)
    opening_time = models.TimeField(auto_now=True)
    closing_time = models.TimeField(auto_now=True)
    device_id = models.CharField(max_length=20, default='')
    hotel_name = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.username

     
class Ssidsignup(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    ssid = models.CharField(max_length=50)
class Specialitysignup(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    speciality = models.CharField(max_length = 30)

# class order(models.Model):
#     user = models.ForeignKey(User)
#








