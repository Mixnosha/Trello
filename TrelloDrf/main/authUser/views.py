from rest_framework import views
from rest_framework.response import Response
from authUser.serializers import RegisterSerializer
from authUser.service import registerUser
import json

class Register(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(request.data)
        registerUser(serializer.data)
        return Response(serializer.data)
