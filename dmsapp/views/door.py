from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from dmsapp.models import Door, Type, Cooler

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
        # A store may not have a cooler before creating a door
        except:
            pass
