from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.timezone import now


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=now)

    def __str__(self):
        return self.username
