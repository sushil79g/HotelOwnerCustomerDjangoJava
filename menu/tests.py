from django.test import TestCase
from .models import Food, Order, Drink
from django.contrib.auth.models import User
from datetime import date


class FoodTest(TestCase):
    def __init__(self):
        name_list = list('abcdefghijklmnopqrstuvwxyz')
        price_list = list('12345678901234567890123456')
        food_type = ['italian' 'local', 'chinese']
        course = ['breakfast', 'luch', 'dinner', 'snacks']
        available = True
        order = None
    
    def create_food(self):
        for i in range(26):
            f = Food(name=self.name_list[i], price=self.price_list[i], food_type=self.food_type[randrage(0, 3)], course=self.course[randrage(0, 4)], available=self.available, order=self.order)



class DrinkTest(TestCase):
    def __init__(self):
        for i in range(26):
            d = Drink(name=self.name_list[i], price=self.price_list[i], food_type=self.food_type[randrage(0, 3)], course=self.course[randrage(0, 4)], available=self.available, order=self.order)


class OrderTest(TestCase):
    def __init__(self):
        user = User()
        user.save()
        order = Order(user=user, date=date.today(), quantity=12)

def main():
    food = FoodTest()
    food.create_food()
    order = OrderTest()
    f.order = 0

main()

