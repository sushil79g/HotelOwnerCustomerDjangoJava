from django.db import models
from django.contrib.auth.models import User
import datetime


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
    # order = models.ForeignKey('Order', null=True, blank=True)
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
    # order = models.ForeignKey('Order', null=True, blank=True)
    image = models.ImageField(upload_to='media/drink/', null=True, blank=True)
    descriptionm = models.TextField(max_length=400, help_text='Enter a short description of this drink', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['drink_type']
    

class FoodOrder(models.Model):
    table_no = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    food = models.ForeignKey('Food', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-time', '-date']



class DrinkOrder(models.Model):
    table_no = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    drink = models.ForeignKey('Drink', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    class Meta:
        ordering = ['-time','-date']

class TodaySpecial(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='', null=True,blank=True)
    description = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=0)
    course_choice = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),    
        ('snacks', 'snacks'),
        ('dinner', 'dinner'),
        )
    course = models.CharField(max_length=30, choices=course_choice, default='snacks')

class SpecialOrder(models.Model):
    table_no = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    special = models.ForeignKey('TodaySpecial', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    # @property
    # def special_name(self):
    #     return self..name
    class Meta:
        ordering = ['-time', '-date']

