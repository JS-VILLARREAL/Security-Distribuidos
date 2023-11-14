from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import View
from ..serializers.view import ViewPublicSerializer

class ViewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = View.objects.all()
    serializer_class = ViewPublicSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ViewPublicSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ViewPublicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        serializer = ViewPublicSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=500)
    
    def destroy(self, request, *args, **kwargs):
        pass
