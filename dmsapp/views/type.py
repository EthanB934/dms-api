from dmsapp.models import Type
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "name")

class TypeViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Queries database with the ORM to list all types 
            types = Type.objects.all()

            # Serializes the list of types into JSON
            serializer = TypeSerializer(types, many=True)

            # Returns the JSON string in a response to the client
            return Response(serializer.data, status=status.HTTP_200_OK)
        # All authenticated users are authorized for this response
        except Exception as ex:
            # If there is any issue with a request to get the types, it is a server error
            return Response(f"There was an error serializing the types data: {ex.args[0]}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    