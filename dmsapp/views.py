# Gives me access to Django's user model, can be extended
from django.contrib.auth.models import User

# Gives me access to Django REST frameworks's ViewSet to create custom views for handling client requests
from rest_framework.viewsets import ViewSet

# Allows me to create new subroutes for specific user requests
from rest_framework.decorators import action

class UserViewSet(ViewSet):
    # This sub route allows for POST and GET operations. The endpoint path defined here will be used in requests to register users
    @action(methods=["post"], url_path="register")

    # At end point /register, this defined method will process a client request to register a new user
    def register_user(self, request):
        pass