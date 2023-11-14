from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import User, Role, View, UserRole, ModuleRole, ViewModule
from ..serializers.user import UserPublicSerializer

class LoginViewsAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Si el usuario y la contraseña son válidos y el state del modelo User es activo osea true, devolver la siguiente información: [usuario, autorización = true].
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=400)

        if user.state:
            # Obtener el rol del usuario.
            role = Role.objects.get(id=UserRole.objects.get(user_id=user.id).role_id).name
            role_id = UserRole.objects.get(user_id=user.id).role_id
            module_access = ModuleRole.objects.filter(role_id=role_id).values_list('module_id', flat=True)
            view_access = ViewModule.objects.filter(module_id__in=module_access).values_list('view_id', flat=True)
            views_active = View.objects.filter(id__in=view_access, state=True).values_list('name', 'description', 'route')

            serializer = UserPublicSerializer(user)
            if views_active.count() > 0:
                return Response({"User": serializer.data, "Authorization": True, "Role": role, "View": views_active}, status=200)
            else:
                return Response({"User":serializer.data, "message": "User has no access to any view"}, status=400)
        else:
            return Response({'message': 'Access denied'}, status=400)