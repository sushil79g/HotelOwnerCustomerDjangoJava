# from django.contrib.auth import get_user_model
# from django.core.exceptions import ObjectDoesNotExist
# # from django.contrib.auth import User
# from .models import UserProfile
# # from django.contrib import Base
from rest_framework import authentication

# class EmailOrMobileAuthBackend(object):
#     def authenticate(self, request):
#         try:
#             user = get_user_model().objects.get(email=request.email)
#             if user.check_password(request.password):
#                 return user
#         except ObjectDoesNotExist:
#             # return None
            
#             # if email.POST.get('email').isdigit():
#             if request.email.isdigit():
#                 try:
#                     user=get_user_model.objects.get(mobile=request.email)
#                     if user.check_password(request.password):
#                         return user
#                 except ObjectDoesNotExist:
#                     return None
    
#     def get_user(self, user_id):
#         try:
#             return get_user_model().objects.get(pk=user_id)
#         except ObjectDoesNotExist:
#             return None


# class DrfAuthBackend(authentication.BaseAuthentication):
#     def authenticate(self, username=None, password=None):
#         try:
#             user = get_user_model().objects.get(email=username)
#             if user.check_password(password):
#                 return user, None
#         except ObjectDoesNotExist:
#             if username.isdigit():
#                 try:
#                     user = get_user_model().objects.get(mobile=username)
#                     if user.check_password(password):
#                         return user, None
#                 except ObjectDoesNotExist:
#                     return None
#             else:
#                 return None


from django.contrib.auth import get_user_model
from .models import UserProfile

class EmailOrMobileAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except UserProfile.ObjectDoesNotExist:
            if username.isdigit():
                try:
                    user = get_user_model().objects.get(mobile=username)
                    if user.check_password(password):
                        return user
                except UserProfile.ObjectDoesNotExist:
                    return None
            else:
                return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except UserProfile.ObjectDoesNotExist:
            return None


class DrfAuthBackend(authentication.BaseAuthentication):
    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user, None
        except UserProfile.DoesNotExist:
            if username.isdigit():
                try:
                    user = get_user_model().objects.get(mobile=username)
                    if user.check_password(password):
                        return user, None
                except UserProfile.DoesNotExist:
                    return None
            else:
                return None