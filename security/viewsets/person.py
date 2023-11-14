from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import Person
from ..serializers.person import PersonPublicSerializer

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Person.objects.all()
    serializer_class = PersonPublicSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = PersonPublicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PersonPublicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        serializer = PersonPublicSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=500)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)

