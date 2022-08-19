from rest_framework import serializers

from boardsApp.serializers import ViewBoardsSerializer
from commentApp.serializers import StatusViewSerializer
from userApp.models import CustomUser
from workSpacesApp.models import WorkSpaces
from workSpacesApp.service import get_slug


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
    status = StatusViewSerializer()

    class Meta:
        model = WorkSpaces
        fields = ['logo', 'status', 'boards', 'title']


class WorkSpaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaces
        fields = ['title', 'status', 'type', 'admin_users']

    def create(self, validated_data):
        adm_user = validated_data.get('admin_users')
        validated_data.pop('admin_users')
        wk = WorkSpaces.objects.create(**validated_data, slug=get_slug(validated_data.get('title')))
        wk.admin_users.add(adm_user[0].id)
        return wk

