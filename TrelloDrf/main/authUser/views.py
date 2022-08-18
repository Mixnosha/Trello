from rest_framework import views
from rest_framework.response import Response
from authUser.serializers import RegisterSerializer
import json
from authUser.service import registerUser


class Register(views.APIView):
    """Регистрация API"""
    def post(self, request):
        serializer = RegisterSerializer(request.data)
        status = registerUser(serializer.data)
        return Response({'status': json.dumps(status)})


class UserStatus(views.APIView):
    """Проверка пользователя на авторизацию"""
    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)
