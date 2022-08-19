from rest_framework import serializers

from boardsApp.serializers import ViewBoardsSerializer
from workSpacesApp.models import WorkSpaces


class CreateWorkspaceSerializer(serializers.ModelSerializer):
    """Создание рабочего пространства """

    class Meta:
        model = WorkSpaces
        fields = ['title', 'status', 'type', 'description']


class ViewAllWorkspacesSerializer(serializers.ModelSerializer):
    """Просмотр всех рабочих пространств"""

    class Meta:
        model = WorkSpaces
        fields = ['id', 'title', 'logo']


class ViewWorkspacesSerializer(serializers.ModelSerializer):
    """Просмотр одного рабочего пространства"""
    boards = ViewBoardsSerializer(many=True)

    class Meta:
        model = WorkSpaces
        fields = ['logo', 'status', 'boards', 'title']


class WorkSpaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaces
        fields = ['title', 'status', 'type']
