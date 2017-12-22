# from django.contrib.auth import authenticate
# from django.contrib.auth import get_user_model
# from .models import Account
# # from rest_framework.authentication import BasicAuthentication
# # from django.contrib.auth.models import B
# from rest_framework import authentication
# class EmailOrMobileAuthBackend(object):
#     def authenticate(self,email=None, password=None):
#         try:
#             user = get_user_model().object.get(email=email)
#             if user.check_password(password):
#                 return user
#         except Account.DoesNotExist:
#             if email.isdigit():
#                 try:
#                     user = get_user_model().object.get(mobile=email)
#                     if user.check_password(password):
#                         return user
#                 except Account.DoesNotExist:
#                     return None
#             else:
#                 return None
#     def get_user(self,user_id):
#         try:
#             return get_user_model().object.get(pk=user_id)
#         except Account.DoesNotExist:
#             return None
#
#
# class DrfAuthBackend(authentication.BaseAuthentication):
#     def authenticate(self, email = None,password=None):
#         try:
#             user = get_user_model().object.get(email=email)
#             if user.check_password(password):
#                 return user, None
#         except Account.DoesNotExist:
#             if email.isdigit():
#                 try:
#                     user = get_user_model().object.get(mobile=email)
#                     if user.check_password(password):
#                         return user, None
#                 except Account.DoesNotExist:
#                     return None
#             else:
#                 return None









from django.contrib.auth import get_user_model
from .models import Account


class EmailOrMobileAuthBackend(object):
    def authenticate(self, email=None, password=None):
        try:
            user = get_user_model().object.get(email=email)
            if user.check_password(password):
                return user
        except Account.DoesNotExist:
            if email.isdigit():
                try:
                    user = get_user_model().object.get(mobile=email)
                    if user.check_password(password):
                        return user
                except Account.DoesNotExist:
                    return None
            else:
                return None

    def get_user(self, user_id):
        try:
            return get_user_model().object.get(pk=user_id)
        except Account.DoesNotExist:
            return None