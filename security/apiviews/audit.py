from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from ..models import User, UserRole, Module, ModuleRole, View, ViewModule

class AuditAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user):
        user_instance = User.objects.filter(username=user).first()
        import pdb; pdb.set_trace()

        if user_instance:
            user_role = UserRole.objects.filter(user=user_instance.id).values('role__id', 'role__name', 'role__state').first()
            role_id = user_role['role__id']
            module_role = ModuleRole.objects.filter(role=role_id).values('module__id', 'module__name', 'module__state').first()
            module_id = module_role['module__id']
            view_module = ViewModule.objects.filter(module=module_id).values('view__id', 'view__name', 'view__state').first()
        else:
            return Response({'message': 'User not found in system'}, status=400)

        permission = {
            'user': user_instance.username,
            'role': {
                    'name': user_role['role__name'],
                    'state': user_role['role__state'],
                },
            'module': {
                    'name': module_role['module__name'],
                    'state': module_role['module__state'],
                },
            'view': {
                    'name': view_module['view__name'],
                    'state': view_module['view__state'],
                }
        }

        if permission:
            return Response(permission, status=200)
        return Response({'message': 'Permission not found in system'}, status=400)