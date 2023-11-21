from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ..models import View

class PracticesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(selft, request):
        # Servicio para contar las vistas eliminadas en la base de datos
        import ipdb; ipdb.set_trace()
        views_deleted = View.objects.filter(deleted__isnull=False).count()
        if views_deleted:
            return Response({'cantidad': views_deleted ,'message': 'Views deleted'}, status=200)
        return Response({'message': 'Views not found'}, status=400)