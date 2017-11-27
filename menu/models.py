from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=30)
    food_type = models.CharField(max_length=30, null=True, blank=True, help_text='Eg: Italian, Continental, Asian')
    course_choice = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),    
        ('snacks', 'snacks'),
        ('dinner', 'dinner'),
        )
    course = models.CharField(max_length=30, choices=course_choice, default='snacks')
    price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    order = models.ForeignKey('Order', null=True, blank=True)
    image = models.ImageField(upload_to='media/food/', null=True, blank=True)
    descriptionm = models.TextField(max_length=400, help_text='Enter a short description of this food', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['course']


class Drink(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, default='local')
    drink_choice = (
        ('soft drink', 'soft drink',),
        ('hard drink', 'hard drink'),     
    )
    drink_type = models.CharField(max_length=30, choices=drink_choice, default='soft drink')
    available = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)
    order = models.ForeignKey('Order', null=True, blank=True)
    image = models.ImageField(upload_to='media/drink/', null=True, blank=True)
    descriptionm = models.TextField(max_length=400, help_text='Enter a short description of this drink', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['drink_type']
    

class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    is_delivered = models.BooleanField(default=False)

