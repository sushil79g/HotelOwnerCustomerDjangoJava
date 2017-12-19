from django.conf.urls import url,include
from . import views
from . import foodorderupdateviews
from rest_framework_jwt.views import obtain_jwt_token
# from .signupview import create_user
from django.db import models
from .views import (
    SignupListView,
    OrderListView,
    PendingListView,
    DeliveredListView,
    # PendingDeliverdListView,
    Foood,
    Drrink,
    Sppecial,
    search,
)
from .foodorderupdateviews import(
    PendingFoodDeliverdListView,
    PendingDrinkDeliverdListView,
    PendingSpecialDeliverdListView,
    FoodListView,
    MenuList,
)
urlpatterns = [
    url(r'^api-token-auth/',obtain_jwt_token),
    url(r'^users/', SignupListView.as_view(), name='list'),
    url(r'^orderlist/',OrderListView.as_view({'get':'list'}), name='orderlist'),
    url(r'^pendinglist/$', PendingListView.as_view({'get':'list'}), name='pendingorderlist'),
    url(r'^deliveredlist/', DeliveredListView.as_view({'get':'list'}), name='deliveredlist'),
    url(r'^pendinglist/food/(?P<pk>\d+)/deliver/$', PendingFoodDeliverdListView.as_view(), name='PendingDeliverdListView'),
    url(r'^pendinglist/drink/(?P<pk>\d+)/deliver/$', PendingDrinkDeliverdListView.as_view(), name='PendingDeliverdListView'),
    url(r'^pendinglist/special/(?P<pk>\d+)/deliver/$', PendingSpecialDeliverdListView.as_view(), name='PendingDeliverdListView'),
    url(r'^menu/$',FoodListView.as_view({'get':'list'}), name='MenuList'),
    url(r'^testing/$',MenuList.as_view(), name='Testing'),
    url(r'^food/',Foood.as_view(), name='Food'),
    url(r'^drink/',Drrink.as_view(), name='Food'),
    url(r'^todayspecial/',Sppecial.as_view(), name='Food'),
    url(r'^search/$',search.as_view({'get':'list'}), name='searching'),
    # url(r'^signup/',create_user,name='create_user'),



    # url(r'drink/all/(?P<pk>\d+)/$', views.FoodRetrieveUpdateDestroy.as_view(), name='allfooddestroy'),


]