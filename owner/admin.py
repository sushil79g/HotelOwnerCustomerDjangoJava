from django.contrib import admin
from .models import Signup, Ssidsignup, Specialitysignup
from menu.models import Food,Drink,Order


# Register your models here.
admin.site.register(Signup)
admin.site.register(Ssidsignup)
admin.site.register(Specialitysignup)
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Order)