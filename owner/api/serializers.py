from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
# from owner.models import Signup
from menu.models import FoodOrder, DrinkOrder, SpecialOrder, Food, Drink, TodaySpecial
from django.contrib.auth.models import User
from owner.models import Signup

class SignupSerializer(ModelSerializer):
    class Meta:
        model = Signup
        fields = [
            'username',
            'email',
            'password',
            'description',

        ]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    # def create(self, validated_data):
    #     user = Signup().objects.create_user(**validated_data)
    #     return user
    # def update(self, instance, validated_data):
    #     if 'password' in validated_data:
    #         password = validated_data.pop('password')
    #         instance.set_password(password)
    #     return super(SignupSerializer, self).update(instance, validated_data)

class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'name',
            'food_type',
            'course',
            'price',
            'available',
            'image',
            'descriptionm',
        ]

class DrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = [
            'name',
            'brand',
            'drink_type',
            'price',
            'available',
            'image',
            'descriptionm',
        ]

class SpecialSerializer(ModelSerializer):
    class Meta:
        model = TodaySpecial
        fields = [
            'name',
            'course',
            'price',
            'image',
            'description',
        ]



class FoodOrderSerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()

    def get_food(self, obj):
        return obj.food.name
    class Meta:
        model = FoodOrder
        fields = [
            'table_no',
            'food',
            'quantity',
            'remarks',
            'delivered'
            # 'food_name'

            ]
class DrinkOrderSerializer(serializers.ModelSerializer):
    drink = serializers.SerializerMethodField()
    def get_drink(selfs,obj):
        return obj.drink.name
    class Meta:
        model = DrinkOrder
        fields = [
            'table_no',
            'drink',
            'quantity',
            'remarks',
            'delivered'

        ]
class SpecialOrderSerializer(serializers.ModelSerializer):
    special = serializers.SerializerMethodField()
    def get_special(selfs,obj):
        return  obj.special.name
    class Meta:
        model = SpecialOrder
        fields = [
            'table_no',
            'special',
            'quantity',
            'remarks',
            'delivered',

            ]

class OrderSerializer(Serializer):
    FoodOrder = FoodOrderSerializer(many=True)
    DrinkOrder = DrinkOrderSerializer(many=True)
    SpecialOrder = SpecialOrderSerializer(many=True)

class OrderPendingSerializer(Serializer):
    FoodOrder = FoodOrderSerializer(many=True)
    DrinkOrder = DrinkOrderSerializer(many=True)
    SpecialOrder = SpecialOrderSerializer(many=True)

class OrderDeliveredSerializer(Serializer):
    FoodOrder = FoodOrderSerializer(many=True)
    DrinkOrder = DrinkOrderSerializer(many=True)
    SpecialOrder = SpecialOrderSerializer(many=True)



# for serach

class FoodSearchSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ['name']

class DrinkSearchSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name']

class SpecialSearchSerializer(ModelSerializer):
    class Meta:
        model = TodaySpecial
        fields = ['name']


class SearchSerializer(Serializer):
    FoodSearch = FoodSearchSerializer(many=True)
    DrinkSearch = DrinkSearchSerializer(many=True)
    SpecialSearch = SpecialSearchSerializer(many=True)




class FoodUpdateSerializer(ModelSerializer):

    class Meta:
        model = FoodOrder
        fields = [
            'id',
        ]

class DrinkUpdateSerializer(ModelSerializer):

    class Meta:
        model = DrinkOrder
        fields = [
            'id',
        ]

class SpecialUpdateSerializer(ModelSerializer):

    class Meta:
        model = SpecialOrder
        fields = [
            'id',
        ]


# menu section


class MenuSectionFoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'name',
            'food_type', #italian, Continential haru
            # 'course', #brakfast, lunch, snacks,dinner
            'price', 
            'available',
            'image',
            'descriptionm',
        ]

    # def to_representation(self, instance):
    #        print(instance.Food.values())
       
        # data = {}
    # for smallItem in bigList:
    #     data[smallItem] = smallItem
        # def to_representation(self , instance):
        
        
    #     Food = super(MenuSectionFoodSerializer, self).to_representation(instance)
        
        
        
    #     # return {
    #     Dfood={'breakfast':{},'lunch':{},'snacks':{},'dinner':{}}
    #     # for 'breakfast' in Food['Food']['course']:
    #     #     Food['breakfast']['']
    #     for a in range(len(Food)):
    #         if Food[a]['course']=='breakfast':
    #             Dfood['breakfast'].update(Food[a])
    #         elif Food[a]['course']=='lunch':
    #             Dfood['lunch'].update(Food[a])
    #         elif Food[a]['course']=='snacks':
    #             Dfood['snacks'].update(Food[a])
    #         elif Food[a]['course']=='dinner':
    #             Dfood['dinner'].update(Food[a])
    #     return Dfood

    #   def to_representation(self, instance):
    #      # instance is the model object. create the custom json format by accessing instance attributes normaly and return it


    #     identifiers = dict()
    #     identifiers['email'] = instance.Email
    #     identifiers['phone'] = instance.phone

    #     representation = {
    #         'identifiers': identifiers,
    #         'activity_type': instance.xxxx,
    #         'timestamp': instance.xxxxx,
    #         .
    #         .
    #         .  -> your custom data
    #      } 

    #  return representation
    # def to_representation(self, instance):
    #     indentifier = dict()
    #     breakfast = dict()
    #     dinner = dict()
    #     snacks = dict()
    #     dinner = dict()
    #     print(type(instance))
    #     print(instance.get('Food'))

    #     for jso in instance.get('Food'):
    #         if jso.course == 'breakfast':
    #             breakfast.update(jso)
    #         elif jso.course == 'dinner':
    #             dinner.update(jso)
    #         elif jso.course=='snacks':
    #             snacks.update(jso)
    #         else:
    #             dinner.update(jso)
        
    #     representation={
    #         'Breakfast': breakfast,
    #         'Dinner': dinner,
    #         'Snacks':snacks
        
    #     }
    #     return representation
        

class MenuSectionDrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = [
            'name',
            'brand', #local international
            # 'drink_type',#soft hard 
            'price', 
            # 'available',
            'image',
            'descriptionm',
        ]


class MenuSectionSpecialSerializer(ModelSerializer):
    class Meta:
        model = TodaySpecial
        fields = [
            'name',
            'course', #snacks 
            'price', 
            'image',
            'description',
        ]


class MenuListSerializer(Serializer):
    FoodBreakfast = MenuSectionFoodSerializer(many=True)
    FoodLunch = MenuSectionFoodSerializer(many=True)
    FoodSnacks = MenuSectionFoodSerializer(many=True)
    FoodDinner = MenuSectionFoodSerializer(many=True)
    DrinkSoft = MenuSectionDrinkSerializer(many=True)
    Beverage =   MenuSectionDrinkSerializer(many=True)
    Special = MenuSectionSpecialSerializer(many=True)





# class SignupSerializer











































































class TestingSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'name',
            'food_type', #italian, Continential haru
             #brakfast, lunch, snacks,dinner
            'price', 
            'available',
            'image',
            'descriptionm',
        ]
