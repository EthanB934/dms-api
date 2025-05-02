from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from dmsapp.models import Door, Type, Cooler
from dmsapp.views.type import TypeSerializer

class DoorSerializer(serializers.ModelSerializer):
    
    type = TypeSerializer(many=False)

    class Meta:
        model = Door
        fields = ("id", "shelves", "slots", "cooler", "type", "door_quantity")

class DoorViewSet(viewsets.ViewSet):
    """
    Route to handle client-requests to door database resource.
    """
    def create(self, request):
        # These steps assume that a cooler has been created 
        # I need a new instance of a door object
        door = Door()

        # I need to extract data from the request body and assign it to the door object'
        try:
            door.shelves = request.data["shelves"]     
            door.slots = request.data["slots"]

            # I need the type object related to this door.
            type = Type.objects.get(pk=request.data["typeId"])

            # Then assign that object to the door
            door.type = type

            # I need the cooler object related to this door 
            cooler = Cooler.objects.get(pk=request.data["coolerId"])

            # Then assign the cooler object to the door
            door.cooler = cooler

            # After I have assigned the request body data to the door object, I need to save that door
            door.save()

            # Serializes the data into JSON for use in response
            serializer = DoorSerializer(door, many=False)

            # Respond to the client if the door was successfully created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # A store may not have a cooler before creating a door
        except Exception as ex:
            return Response(f"There was an issue while creating the door: {ex}", status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        # Gets all doors associated with the cooler the user clicked
        doors = Door.objects.filter(cooler=pk)
        
        # Serializes the list of filtered doors into JSON for use in response
        serializer = DoorSerializer(doors, many=True)

        # Returns a response to the client with a JSON string of door objects
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        door = Door.objects.get(pk=pk)
        try:
            door.shelves = request.data["shelves"]     
            door.slots = request.data["slots"]
            type = Type.objects.get(pk=request.data["typeId"])
            door.type = type
            cooler = Cooler.objects.get(pk=request.data["coolerId"])
            door.cooler = cooler
            door.save()
            return Response(f"Door {pk} has been successfully updated", status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f"There has been an issue updating this cooler door: {ex}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)