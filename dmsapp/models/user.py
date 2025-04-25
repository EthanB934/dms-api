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
    password = models.CharField(max_length=100)
    
    # Overwrites the save method of the AbstractUser given by Django
    # Accepts all arguments and keyword arguments as usual
    def save(self, *args, **kwargs):
        # I am not expecting my users to have a username, but rather an email
        if not self.username:
            # Assigns users emails to their usernames to meet Django's unique constraint
            self.username = self.email
        # Calls the rest of the save method defined on the AbstractUser class
        super().save(*args, **kwargs)