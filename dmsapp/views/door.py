from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from dmsapp.models import Door

class DoorViewSet(viewsets.ViewSet):
    """
    Route to handle client-requests to door database resource.
    """
    def create(self, request):
        