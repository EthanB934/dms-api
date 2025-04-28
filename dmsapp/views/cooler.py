from dmsapp.models import Cooler, StoreAsUser, Door
from dmsapp.views.type import TypeSerializer
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

class CoolerSerializer(serializers.ModelSerializer):
    cooler_types = serializers.SerializerMethodField()

    def get_cooler_types(self, obj):
        # Queries the doors table for the doors related to the cooler
        doors = Door.objects.filter(cooler=obj.id)
        types = []
        # Returns the name of the product type offered by each door to be listed on the cooler
        for door in doors:
            # appends each door type to the types list
            types.append(door.type)
        # Serializes the types found in each for door per cooler
        serializer = TypeSerializer(types, many=True)

        # assigns the return value to the cooler_types
        return serializer.data

    class Meta:
        model = Cooler
        fields = ("id", "total_capacity", "cooler_types")

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

    def list(self, request):
        # Filters coolers by requesting authenticated user
        coolers = Cooler.objects.filter(stores=request.auth.user)

        # Serializes filtered list of coolers in JSON for use in response to client
        serializer = CoolerSerializer(coolers, many=True)

        # Returns serialized list of cooler objects as JSON to client
        return Response(serializer.data, status=status.HTTP_200_OK)
    