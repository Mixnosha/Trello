from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from cardsApp.models import Cards
from cardsApp.serializers import OneCardViewSerializer



@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Получение всех досок  залогиненого пользователя"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создание доски "
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Получение одной доски залогиненного пользователя"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удаление доски"
))
class CardsCRUD(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cards.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OneCardViewSerializer
    