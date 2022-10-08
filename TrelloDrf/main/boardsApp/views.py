from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from boardsApp.models import Boards
from boardsApp.serializers import BoardCreateSerializer, BoardViewSerializers, BoardUpdateSerializers, \
    ViewBoardsSerializer


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
class BoardsModelView(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Boards.objects.filter(workspaces_boards=self.kwargs['id'])
            
        else:
            return Boards.objects.filter(admin_users__user__username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return BoardViewSerializers
        if self.action == 'create':
            return BoardCreateSerializer
        if self.action == 'retrieve':
            return ViewBoardsSerializer
        if self.action == 'update':
            return BoardUpdateSerializers

