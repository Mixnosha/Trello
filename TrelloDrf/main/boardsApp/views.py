from django.shortcuts import render
from rest_framework import viewsets

from boardsApp.models import Boards
from boardsApp.serializers import BoardCreateSerializer, BoardViewSerializers, BoardUpdateSerializers


class BoardsModelView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Boards.objects.filter(admin_users__user__username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            print(self.request.POST['wk_id'])
            return BoardCreateSerializer
        if self.action == 'list':
            return BoardViewSerializers
        if self.action == 'update':
            return BoardUpdateSerializers

