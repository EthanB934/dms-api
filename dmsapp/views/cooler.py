from dmsapp.models import Cooler, StoreAsUser
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

class CoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooler
        fields = ("id", "total_capacity")

class CoolerViewSet(viewsets.ViewSet):
    def create(self, request):
        # Instantiates a new cooler that the user wants to create
        cooler = Cooler()

        # Creates the cooler in the database
        cooler.save()

        # Gets the requesting user creating the new cooler
        user = request.auth.user

        # Adds the cooler and the user to the many-to-many relationship table between them
        user.coolers.add(cooler)

        # Serialize the cooler object. The client will require the cooler's id when creating doors
        serializer = CoolerSerializer(cooler, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

