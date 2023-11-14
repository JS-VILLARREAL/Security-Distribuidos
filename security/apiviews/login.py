from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate

from ..models import User, Role, UserRole
from ..serializers.user import UserPublicSerializer

class LoginAPIView(APIView):
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

        import pdb; pdb.set_trace()
        if user.state:
            serializer = UserPublicSerializer(user)

            return Response({"User": serializer.data, "Authorization": True}, status=200)
        else:
            return Response({'message': 'Account is disabled'}, status=400)