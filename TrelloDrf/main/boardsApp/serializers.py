from rest_framework import serializers

from boardsApp.service import get_slug_board
from workSpacesApp.models import WorkSpaces
from boardsApp.models import Boards
from userApp.models import CustomUser
from workSpacesApp.service import get_slug


class ViewBoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ['id', 'title', 'background']


class BoardCreateSerializer(serializers.ModelSerializer):
    """ Создание доски для рабочего пространства"""
    slug = serializers.CharField(required=False)

    class Meta:
        model = Boards
        fields = ['title', 'status', 'slug']

    def create(self, validated_data):
        adm_user = CustomUser.objects.get(user__username=self.context['request'].user)
        board = Boards.objects.create(
            **validated_data,
            slug=get_slug_board(validated_data.get('title'))
        )
        board.admin_users.add(adm_user.id)
        board.title = board.title
        board.save()
        wk = WorkSpaces.objects.get(id=self.context['request'].POST['wk_id'])
        wk.boards.add(board.id)
        wk.save()
        return board


class BoardViewSerializers(serializers.ModelSerializer):
    """Просмотр всех досок пользователя """
    class Meta:
        model = Boards
        fields = ['id', 'title', 'background']



