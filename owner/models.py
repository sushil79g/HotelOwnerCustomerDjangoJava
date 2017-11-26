from django.db import models
from django.core.validators import RegexValidator


class Signup(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=50, validators=[RegexValidator(regex='^.{8}$', message='Minimum 8 character required!!!', code='nomatch')])
    token = models.CharField(max_length = 150)
    description = models.CharField(max_length  = 250)
    extra_charge = models.BooleanField(default=False)
    vat = models.BooleanField(default = True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    device_id = models.CharField(max_length=20)

     
class Ssidsignup(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    ssid = models.CharField(max_length=50)
class Specialitysignup(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    speciality = models.CharField(max_length = 30)



