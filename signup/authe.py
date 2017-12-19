from django.contrib.auth import get_user_model
from django.contrib.auth import User
# from django.contrib import Base
from rest_framework import authentication

class EmailOrMobileAuthBackend(object):
    def authenticate(self, email=None,password=None):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExit:
            # return None
            if email.isdigit():
                try:
                    user=get_user_model.objects.get(mobile=email)
                    if user.check_password(password):
                        return user
                except User.DoesNotExit:
                    return None
    
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except User.DoesNotExit:
            return None


class DrfAuthBackend(authentication.BaseAuthentication):
    def authenticate(self, username=None, password=None):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user, None
        except User.DoesNotExit:
            if username.isdigit():
                try:
                    user = get_user_model().objects.get(mobile=username)
                    if user.check_password(password):
                        return user, None
                except User.DoesNotExit:
                    return None
            else:
                return None


