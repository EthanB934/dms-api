# Gives me access to Django's user model, can be extended
from dmsapp.models import StoreAsUser

# Gives me access to Django REST frameworks's ViewSet to create custom views for handling client requests
from rest_framework.viewsets import ViewSet

# Gives me access to Django REST framework's Serializer class from which my custom serializer classes will inherit
from rest_framework.serializers import ModelSerializer, SerializerMethodField

# Gives me access to DRF's response class that can be sent and seen by a user
from rest_framework.response import Response

# Gives me access to all of DRF's defined status codes to use in responses to clients
from rest_framework import status, permissions

# Gives access to ORM to query the Token data table
from rest_framework.authtoken.models import Token

# Allows me to create new subroutes for specific user requests
from rest_framework.decorators import action

class UserSerializer(ModelSerializer):
    """A class that handles the serialization of user data, whether for saving to the database or 
    responding to the client with queried data

    Args:
        ModelSerializer (class): A class that serializes data patterned after a given model
    """
    token = SerializerMethodField()

    def get_token(self, obj):
        return self.context["token"].key
    
    class Meta:
        """Required class by DRF's ModelSerializer. 
        Choose which models and which fields from that model to serialize."""

    
        model = StoreAsUser
        fields = ("id", "email", "username", "store_number", "store_name", "address", "token")

class UserViewSet(ViewSet):
    """A view used to handle new user registration. Supports POST requests

    Args:
        ViewSet (class): A class inherited from rest framework. It comes with predefined methods
        used for supporting different HTTP commands
    """
    # Because of DRF's security measures, authorization is needed for all requests. 
    # However, view set should not. A user is receiving the credentials needed for authorization in this view
    permission_classes = [permissions.AllowAny]

    @action(methods=["post"], detail=False, url_path="register")
    
    # At end point /register, this defined method will process a client request to register a new user
    def register_user(self, request):
        """Method used to create new users"""
        # Instantiate a new User object
        new_user = StoreAsUser()

        try:
            # Extends properties of User object to include custom user fields
            new_user.email = request.data["email"]
            new_user.username = new_user.email
            new_user.store_number = request.data["storeNumber"]
            new_user.store_name = request.data["storeName"]
            new_user.address = request.data["address"]

            # Saves registering user's data to database
            new_user.save()

            #  Get or create a token for a user
            token, created = Token.objects.get_or_create(user=new_user)

            new_user.token = token.key
            # Serializes user data according to my desired pattern
            serializer = UserSerializer(new_user, many=False,  context={"token": token})
             
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(f'There has been an issue registering this user: {ex.args}', status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=["post"], detail=False, url_path="login")
    def login_user(self, request):  
        pass