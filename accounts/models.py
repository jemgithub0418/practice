from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email',]
    address = models.CharField(max_length= 250)
