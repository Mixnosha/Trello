from rest_framework import serializers

from boardsApp.models import Boards


class ViewBoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ['id', 'title', 'background']
