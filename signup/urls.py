from django.conf.urls import url
# from .views import create_user
from .views import UserSignUp,UserListSignUp

urlpatterns=[
    url(r'^signup/',UserSignUp.as_view(), name='create_user'),
    url(r'^show/',UserListSignUp.as_view(), name='list user'),
    url(r'^update/(?P<id>\d+)$',UserUpdateSignUp.as_view(), name='update_user'),
]