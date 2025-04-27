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
            types = Type.objects.all()
            serializer = TypeSerializer(types, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f"There was an error serializing the types data: {ex.args[0]}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
