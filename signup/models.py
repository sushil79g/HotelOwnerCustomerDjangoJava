from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    # username = models.CharField(max_length=256,default='')
    # email = models.EmailField(unique=True, max_length=250)
    # password = models.CharField(max_length=50, validators=[RegexValidator(regex='^.{8}$', message='Minimum 8 character required!!!', code='nomatch')])
    # token = models.CharField(max_length=150, default='')
    user = models.OneToOneField(User,primary_key=True, related_name = 'profile')
    mobile = models.IntegerField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, default='')
    extra_charge = models.BooleanField(default=False)
    vat = models.BooleanField(default=True)
    opening_time = models.TimeField(auto_now=True)
    closing_time = models.TimeField(auto_now=True)
    device_id = models.CharField(max_length=20, default='')
    hotel_name = models.CharField(max_length=150, default='')
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance=None,created=False, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

# @receiver(pre_delete, sender=User)
# def delete_profile_for_user(sender,instance= None,**kwargs):
#     # instance.profile.save()
#     if instance:
#         user_profile = UserProfile.objects.get(user=instance)
#         user_profile.delete()

     
# class Ssidsignup(models.Model):
#     signup = models.ForeignKey(User, on_delete=models.CASCADE)
#     ssid = models.CharField(max_length=50)
# class Specialitysignup(models.Model):
#     signup = models.ForeignKey(User, on_delete=models.CASCADE)
#     speciality = models.CharField(max_length = 30)
