from rest_framework.generics import ListAPIView,UpdateAPIView, RetrieveUpdateDestroyAPIView,  RetrieveUpdateAPIView
from django.contrib.auth.models import User
from itertools import chain
from operator import attrgetter
from rest_framework.response import Response
from rest_framework import serializers
from owner.models import Signup
from menu.models import FoodOrder, DrinkOrder, SpecialOrder, Food, Drink, TodaySpecial
from .serializers import SignupSerializer, FoodOrderSerializer, DrinkOrderSerializer, SpecialOrderSerializer, OrderSerializer, FoodSerializer, DrinkSerializer,SpecialSerializer
from collections import namedtuple
from rest_framework import viewsets
import datetime
from rest_framework.views import APIView
from rest_framework import status

class SignupListView(ListAPIView):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer




Order = namedtuple('Order', ('FoodOrder', 'DrinkOrder', 'SpecialOrder'))
class OrderListView(viewsets.ViewSet):
    # serializer_class = OrderSerializer

    def list(self, request):
        date = datetime.date.today()
        timeline = Order(
            FoodOrder = FoodOrder.objects.filter(date= date),
            DrinkOrder =DrinkOrder.objects.filter(date=date),
            SpecialOrder = SpecialOrder.objects.filter(date=date)
        )
        serial = OrderSerializer(timeline)
        return Response(serial.data)
    # queryset = User.objects.all() | FoodOrder.objects.all() | DrinkOrder.objects.all() |SpecialOrder.objects.all()
    # queryset = list(chain(FoodOrder.objects.all(), DrinkOrder.objects.all(),SpecialOrder.objects.all() ))


class PendingListView(viewsets.ViewSet):
    # serializer_class = OrderSerializer

    def list(self, request):
        date = datetime.date.today()
        timeline = Order(
            FoodOrder = FoodOrder.objects.filter(delivered=False, date = date),
            DrinkOrder =DrinkOrder.objects.filter(delivered=False, date=date),
            SpecialOrder = SpecialOrder.objects.filter(delivered=False, date=date)
        )
        serial = OrderSerializer(timeline)
        return Response(serial.data)

class DeliveredListView(viewsets.ViewSet):
    # serializer_class = OrderSerializer

    def list(self, request):
        date = datetime.date.today()
        timeline = Order(
            FoodOrder=FoodOrder.objects.filter(delivered=True, date=date),
            DrinkOrder=DrinkOrder.objects.filter(delivered=True, date=date),
            SpecialOrder=SpecialOrder.objects.filter(delivered=True, date=date)
        )
        serial = OrderSerializer(timeline)
        return Response(serial.data)
        # queryset = User.objects.all() |






                # queryset = User.objects.all() |




# class AllFoodRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer



# def order(self):
#     food = FoodOrder.objects.all()
#     drink = DrinkOrder.objects.all()
#     special = SpecialOrder.objects.all()
#
#     serial1 = FoodOrderSerializer(food, many=True).data
#     serial2 = DrinkOrderSerializer(drink, many=True).data
#     serial3 = SpecialOrderSerializer(special, many=True).data
#
#     chain_list = sorted(serial1 +serial2 +serial3, key=lambda x: x.get('user'))
#     return  Response(chain_list)




# menu section








# class PendingDeliverdListView(UpdateAPIView):
#     queryset = FoodOrder.objects.get()
#     serializer_class = FoodOrderSerializer
#     def partial_update(self, request, *args, **kwargs):
#         # serializer.save(delivered=True)
#         instance = self.get_object()
#         instance.delivered = True
#         instance.save(update_fields = ['delivered'])
#         return Response()


# class OrderDelivered(UpdateAPIView):
#     queryset = FoodOrder.objects.all()
#     serializer_class = FoodOrderSerializer

# class PendingDeliverdListView(RetrieveUpdateAPIView):
    # serializer_class = FoodOrderSerializer
    # queryset = FoodOrder.objects.all()
    # # def get_queryset(self):
    # #     queryset = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    # #     print('hello world')
    # #     return queryset
    
    # # def perform_update(self, serializer):
    # #     food_obj = FoodOrder.objects.filter(pk=self.kwargs['pk'])
    # #     print('perform_update')
    # #     food_obj.delivered = True
    # #     serializer.update()

    # def update(self, request, *args, **kwargs):
    #     food_obj = self.get_object()
    #     food_obj.delivered = True
    #     food_obj.save()

    #     serializer = self.get_serializer(data = food_obj)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)





class Food(APIView):
    def get(self, request, format=None):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Drink(APIView):
    def get(self, request, format=None):
        drink = Drink.objects.all()
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = DrinkSerializer(date=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Special(APIView):
    def get(self, request, format=None):
        drink = TodaySpecial.objects.all()
        serializer = SpecialSerializer(drink)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = SpecialSerializer(date=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    