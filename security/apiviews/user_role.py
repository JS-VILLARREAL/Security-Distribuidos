from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ..models import UserRole

class UserRoleInactiveAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Se obtiene la lista de usuarios con roles inactivos
        users = UserRole.objects.filter(role__state=False).values('user__username', 'role__name', 'user__state', 'role__state').all()
        if users:
            return JsonResponse({'users': list(users)})
        return JsonResponse({'message': 'No users with inactive roles'}, status=400)