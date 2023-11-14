from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from ..models import View, Module, Role, ViewModule

class ViewsInfoAPIView(APIView):
    permission_classes = [AllowAny]
    #Recibir un parámetro booleano; si es true, mostrar todas las vistas activas para el sistema, y si es false, mostrar solo las inactivas.
    def get(self, request, state):
        import ipdb; ipdb.set_trace()
        if state == 'true':
            views = View.objects.filter(state=True)
        elif state == 'false':
            views = View.objects.filter(state=False)
        else:
            return Response({'message': 'Invalid parameter'}, status=status.HTTP_400_BAD_REQUEST)
        views = views.values('id', 'name', 'description', 'route')
        return Response(views, status=status.HTTP_200_OK)