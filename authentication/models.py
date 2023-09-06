from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth.models import User


class User(AbstractUser):
    
    def __str__(self):
        return self.email
