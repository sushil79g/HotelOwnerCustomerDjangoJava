from django.db import models
# from django.contrib.auth.models import  User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# from rest_framework.excep
# Create your models here.
# class account(models.Model):
#     # user = models.OneToOneField(User)
#     user = models.OneToOneField(User, primary_key=True, related_name='profile')
#     mobile = models.IntegerField(unique=True)
#     createdid_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     description = models.CharField(max_length=250)
#     extra_charge = models.BooleanField(default=False)
#     vat = models.BooleanField(default=True)
#     opening_time = models.TimeField(auto_now=True)
#     closing_time = models.TimeField(auto_now=True)
#     device_id = models.CharField(max_length=20, default='')
#     hotel_name = models.CharField(max_length=150, default='')
#     is_verify = models.BooleanField(default=False)

class AccountManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('user must have a valid email address')
        if not kwargs.get('mobile'):
            raise ValueError('User must have a valid number')

        account = self.model(
            email = self.normalize_email(email),
            mobile = kwargs.get('mobile'),
            description =kwargs.get('description'),
            extra_charge = kwargs.get('extra_charge'),
            vat = kwargs.get('vat'),
            device_id = kwargs.get('device_id'),
            hotel_name = kwargs.get('hotel_name'),

        )
        account.set_password(password)
        account.is_admin=False
        account.save()
        return account
    def create_superuser(self,email,password=None,**kwargs):
        account = self.create_user(email,password,**kwargs)
        account.is_admin =True
        # account.is_staff=True
        account.save()
        return  account


class Account(AbstractBaseUser,PermissionsMixin):
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    description = models.CharField(max_length=250,default='',null=True,)
    extra_charge = models.NullBooleanField(default=None)
    vat = models.NullBooleanField(default=None)
    opening_time = models.TimeField(auto_now=True)
    closing_time = models.TimeField(auto_now=True)
    device_id = models.CharField(max_length=20, default='',null=True)
    hotel_name = models.CharField(max_length=150, default='',null=True)
    is_verify = models.BooleanField(default=False)
    # is_admin =
    is_admin = models.BooleanField(default=False)
    is_superuser = models.IntegerField(default=False)

    object = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    def get_full_name(self):
        return ''.join(self.email)

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

