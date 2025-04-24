from django.db import models

# Allows me to customize Django's preset User model
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StoreAsUser(AbstractUser):
    """A custom user model representing a store as a user

    Args:
        AbstractUser (class): Customizable user model, similar to User, but can hold new fields
    """
    email = models.EmailField(max_length=155)
    store_name = models.CharField(max_length=100)
    store_number = models.IntegerField()
    address = models.CharField(max_length=255)
    