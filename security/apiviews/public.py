from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Person, User, Role, Module, View
from ..serializers.person import PersonPublicSerializer
from ..serializers.user import UserPublicSerializer
from ..serializers.role import RolePublicSerializer
from ..serializers.module import ModulePublicSerializer
from ..serializers.view import ViewPublicSerializer


class ListsAPIView(APIView):
    permission_classes = ()

    def get(self, request):
        person = Person.objects.filter().all()
        user = User.objects.filter().all()
        role = Role.objects.filter().all()
        module = Module.objects.filter().all()
        view = View.objects.filter().all()

        return Response({
            "persons": PersonPublicSerializer(person, many=True).data,
            "users": UserPublicSerializer(user, many=True).data,
            "roles": RolePublicSerializer(role, many=True).data,
            "modules": ModulePublicSerializer(module, many=True).data,
            "views": ViewPublicSerializer(view, many=True).data,
        })