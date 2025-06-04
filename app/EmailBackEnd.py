from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None , password = None , **kwargs) : 
        # when you want a function to accept an arbitrary number of keyword arguments without knowing in advance what they will be.
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None