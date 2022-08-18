from rest_framework import serializers

from workSpacesApp.models import WorkSpaces


class CreateWorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaces
        fields = ['title', 'status', 'type', 'description']

class ViewAllWorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaces
        fields = ['id', 'title', 'logo']

class ViewWorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaces
        fields = ['logo', 'status', 'boards', 'title']
#Дописать сериалайзер на Boards