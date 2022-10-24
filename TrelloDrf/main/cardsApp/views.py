from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from cardsApp.models import Cards
from cardsApp.serializers import OneCardViewSerializer, AllCardViewSerializer, CreateCardSerializer, \
    UpdateCardSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Получение всех карточек  залогиненого пользователя"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создание карточки (параметр clmn_id id доски к которой привязываемся)"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Получение одной карточки залогиненного пользователя"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удаление карточки"
))
class CardsCRUD(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Cards.objects.filter(column_cards=self.kwargs['id'])
        else:
            return Cards.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AllCardViewSerializer
        if self.action == 'retrieve':
            return OneCardViewSerializer
        if self.action == 'create':
            return CreateCardSerializer
        if self.action == 'update':
            return UpdateCardSerializer
    