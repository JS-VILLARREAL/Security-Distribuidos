from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import User
from ..serializers.user import UserPublicSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=400)

        if user.state:
            serializer = UserPublicSerializer(user)
            return Response({'User': serializer.data, 'Authorization': True}, status=200)
        else:
            return Response({'message': 'Account is disabled'}, status=400)