# Gives me access to Django's user model, can be extended
from django.contrib.auth.models import User

# Gives me access to Django REST frameworks's ViewSet to create custom views for handling client requests
from rest_framework.viewsets import ViewSet

# Gives me access to Django REST framework's Serializer class from which my custom serializer classes will inherit
from rest_framework.serializers import ModelSerializer

# Gives me access to DRF's response class that can be sent and seen by a user
from rest_framework.response import Response

# Gives me access to all of DRF's defined status codes to use in responses to clients
from rest_framework import status

# Allows me to create new subroutes for specific user requests
from rest_framework.decorators import action

class UserSerializer(ModelSerializer):
    """A class that handles the serialization of user data, whether for saving to the database or 
    responding to the client with queried data

    Args:
        ModelSerializer (class): A class that serializes data patterned after a given model
    """
    class Meta:
        """Required class by DRF's ModelSerializer. 
        Choose which models and which fields from that model to serialize."""
        model = User
        fields = ("id", "email", "store_number", "store_name", "address")

class UserViewSet(ViewSet):
    """A view used to handle new user registration. Supports POST requests

    Args:
        ViewSet (class): A class inherited from rest framework. It comes with predefined methods
        used for supporting different HTTP commands
    """
    @action(methods=["post"], url_path="register")

    # At end point /register, this defined method will process a client request to register a new user
    def register_user(self, request):
        """Method used to create new users"""
        # Instantiate a new User object
        new_user = User()

        try:
            # Extends properties of User object to include custom user fields
            new_user.email = request.data["email"]
            new_user.store_number = request.data["storeNumber"]
            new_user.store_name = request.data["storeName"]
            new_user.address = request.data["address"]

            # Saves registering user's data to database
            new_user.save()

            # Serializes user data according to my desired pattern
            serializer = UserSerializer(new_user, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(f'There has been an issue registering this user: {ex.args[0]}', status=status.HTTP_400_BAD_REQUEST)