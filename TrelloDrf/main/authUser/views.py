from rest_framework import views
from rest_framework.response import Response
from authUser.serializers import RegisterSerializer
from authUser.service import registerUser
import json

class Register(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(request.data)
        status = registerUser(serializer.data)
        return Response({'status': json.dumps(status)})

