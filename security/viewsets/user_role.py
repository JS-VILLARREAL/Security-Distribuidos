from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import UserRole, User, Role
from ..serializers.user_role import UserRolePublicSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserRole.objects.all()
    serializer_class = UserRolePublicSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UserRolePublicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserRolePublicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
