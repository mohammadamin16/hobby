from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self,username,name, password=""):
        username = username
        password = password
        name     = name
        user = self.model(
            username=username,
            password=password,
            name=name
        )





class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name     = models.CharField(max_length=100)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password']



