from rest_framework import views, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from authUser.serializers import RegisterSerializer, LoginSerializer
from authUser.service import registerUser, login
import json


class Register(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(request.data)
        status = registerUser(serializer.data)
        return Response({'status': json.dumps(status)})


class Login(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(request.data)
        login(serializer.data)
        print(request.user.is_authenticated)
        return Response({'status': 'true'})


class UserStatus(views.APIView):

    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)
