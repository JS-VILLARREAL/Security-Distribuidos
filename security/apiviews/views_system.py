from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from ..models import View, Module, Role, ViewModule, ModuleRole

class ViewsInfoAPIView(APIView):
    permission_classes = [AllowAny]
    #Recibir un parámetro booleano; si es true, mostrar todas las vistas activas para el sistema, y si es false, mostrar solo las inactivas.
    def get(self, request, state):
        if state == 'true':
            views = View.objects.filter(state=True)
        elif state == 'false':
            views = View.objects.filter(state=False)
        else:
            return Response({'message': 'Invalid parameter'}, status=status.HTTP_400_BAD_REQUEST)

        view_module = ViewModule.objects.filter(view__in=views).values('module').distinct()
        modules = Module.objects.filter(id__in=view_module)
        module_role = ModuleRole.objects.filter(module__in=modules).values('role').distinct()
        roles = Role.objects.filter(id__in=module_role)

        response_data = {
            "views": views.values('name', 'state'),
            "module": modules.values('name', 'state'),
            "role": roles.values('name', 'state')
        }

        return Response(response_data, status=status.HTTP_200_OK)