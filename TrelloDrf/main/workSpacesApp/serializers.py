from rest_framework import serializers
from boardsApp.serializers import ViewBoardsSerializer
from status.models import StatusWK
from status.serializers import StatusViewSerializer
from userApp.models import CustomUser
from userApp.serializers import CustomUserViewAllSerializer
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
        fields = ['id', 'title', 'logo', 'slug']


class ViewOneWorkspacesSerializer(serializers.ModelSerializer):
    """Просмотр одного рабочего пространства"""
    boards = ViewBoardsSerializer(many=True)
    status = StatusViewSerializer()
    type = serializers.CharField(source='get_type_display')
    admin_users = CustomUserViewAllSerializer(many=True)

    class Meta:
        model = WorkSpaces
        fields = [
            'logo',
            'status',
            'boards',
            'title',
            'users',
            'type',
            'web_site',
            'description',
            'join_link',
            'admin_users',
            'slug',
        ]


class WorkSpaceCreateSerializer(serializers.ModelSerializer):
    """Создание рабочего пространства"""
    slug = serializers.CharField(required=False)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = WorkSpaces
        fields = ['id', 'title', 'status', 'type', 'description', 'slug']

    def create(self, validated_data):
        adm_user = CustomUser.objects.get(user__username=self.context['request'].user)
        wk = WorkSpaces.objects.create(
            **validated_data,
            slug=get_slug(validated_data.get('title'))
        )
        wk.admin_users.add(adm_user.id)
        wk.title = wk.title
        wk.save()
        return wk


class UpdateWorkspacesSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    status = StatusViewSerializer(required=False)
    slug = serializers.CharField(required=False)
        
    class Meta:
        model = WorkSpaces
        fields = ('title', 'logo', 'description', 'web_site', 'type', 'status', 'slug')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.web_site = validated_data.get('web_site', instance.web_site)
        instance.type = validated_data.get('type', instance.type)
        if 'status' in validated_data:
            print('sdfsdfsdfgsdfygs')
            instance.status = StatusWK.objects.get(title=validated_data['status']['title'])
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance





