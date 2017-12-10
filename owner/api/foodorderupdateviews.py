from rest_framework.generics import ListAPIView,UpdateAPIView, RetrieveUpdateDestroyAPIView,  RetrieveUpdateAPIView
from menu.models import FoodOrder, DrinkOrder, SpecialOrder
from .serializers import FoodUpdateSerializer, DrinkUpdateSerializer, SpecialUpdateSerializer, MenuListSerializer,TestingSerializer
from rest_framework.response import Response
from collections import namedtuple
from rest_framework import viewsets
from menu.models import Food, Drink, TodaySpecial
from rest_framework.views import APIView



class PendingFoodDeliverdListView(RetrieveUpdateAPIView):
    serializer_class = FoodUpdateSerializer
    queryset = FoodOrder.objects.all()
    # def get_queryset(self):
    #     queryset = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('hello world')
    #     return queryset
    
    # def perform_update(self, serializer):
    #     food_obj = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('perform_update')
    #     food_obj.delivered = True
    #     serializer.update()

    def update(self, request, *args, **kwargs):
        food_obj = self.get_object()
        food_obj.delivered = True
        food_obj.save()

        serializer = self.get_serializer(data = food_obj)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class PendingDrinkDeliverdListView(RetrieveUpdateAPIView):
    serializer_class = DrinkUpdateSerializer
    queryset = DrinkOrder.objects.all()
    # def get_queryset(self):
    #     queryset = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('hello world')
    #     return queryset
    
    # def perform_update(self, serializer):
    #     food_obj = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('perform_update')
    #     food_obj.delivered = True
    #     serializer.update()

    def update(self, request, *args, **kwargs):
        food_obj = self.get_object()
        food_obj.delivered = True
        food_obj.save()

        serializer = self.get_serializer(data = food_obj)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class PendingSpecialDeliverdListView(RetrieveUpdateAPIView):
    serializer_class = SpecialUpdateSerializer
    queryset = SpecialOrder.objects.all()
    # def get_queryset(self):
    #     queryset = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('hello world')
    #     return queryset
    
    # def perform_update(self, serializer):
    #     food_obj = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    #     print('perform_update')
    #     food_obj.delivered = True
    #     serializer.update()

    def update(self, request, *args, **kwargs):
        food_obj = self.get_object()
        food_obj.delivered = True
        food_obj.save()

        serializer = self.get_serializer(data = food_obj)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)





# Menu Section


list = namedtuple('list',('FoodBreakfast','FoodLunch','FoodSnacks','FoodDinner','DrinkSoft','Beverage','Special'))


class FoodListView(viewsets.ViewSet):
    def list(self,request):
        timeline = list(
            FoodBreakfast = Food.objects.filter(course='breakfast'),
            FoodLunch = Food.objects.filter(course='lunch'),
            FoodSnacks = Food.objects.filter(course='snacks'),
            FoodDinner = Food.objects.filter(course='dinner'),
            DrinkSoft = Drink.objects.filter(drink_type='soft drink'),
            Beverage = Drink.objects.filter(drink_type='hard drink'),
            Special = TodaySpecial.objects.all()
        )
        serial = MenuListSerializer(timeline)
        # breakfast = Food.objects.filter(course = 'breakfast')
        # breakfastSerializer = TestingSerializer(breakfast, many=True)
        # lunch = Food.objects.filter(course='lunch')
        # lunchserialize = TestingSerializer(lunch, many=True)
        # snacks = Food.objects.filter(course='snacks')
        # snacksSerializer = TestingSerializer(snacks, many=True)
        return Response(serial.data)



# list = namedtuple('list',('Drink','Special'))


# class FoodListView(viewsets.ViewSet):
#     def list(self,request):
#         timeline = list(
#             # Food = Food.objects.all(),
#             Drink = Drink.objects.all(),
#             Special = TodaySpecial.objects.all()
#         )
#         serial = MenuListSerializer(timeline)
#         breakfast = Food.objects.filter(course = 'breakfast')
#         breakfastSerializer = TestingSerializer(breakfast, many=True)
#         lunch = Food.objects.filter(course='lunch')
#         lunchserialize = TestingSerializer(lunch, many=True)
#         snacks = Food.objects.filter(course='snacks')
#         snacksSerializer = TestingSerializer(snacks, many=True)
#         return Response(serial.data,{'breakfast':breakfastSerializer.data,'lunch':lunchserialize.data, 'snacks':snacksSerializer.data})



class MenuList(APIView):
    def get(self, request, format=None):
        breakfast = Food.objects.filter(course = 'breakfast')
        breakfastSerializer = TestingSerializer(breakfast, many=True)
        lunch = Food.objects.filter(course='lunch')
        lunchserialize = TestingSerializer(lunch, many=True)
        snacks = Food.objects.filter(course='snacks')
        snacksSerializer = TestingSerializer(snacks, many=True)
        # dinner = Food.objects.filter(course='dinner')
        # dinnerSerializer = TestingSerializer(dinner, many=True)
        return Response({'breakfast':breakfastSerializer.data,'lunch':lunchserialize.data, 'snacks':snacksSerializer.data})
