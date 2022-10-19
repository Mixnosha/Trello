from rest_framework import serializers

from boardsApp.models import Boards
from columnApp.models import Column
from userApp.models import CustomUser


class ColumnAllViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        depth = 1
        fields = ['id', 'title', 'cards']


class ColumnOneViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        depth = 1
        fields = '__all__'


class CreateColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('title', 'id')

    def create(self, validated_data):
        adm_user = CustomUser.objects.get(user__username=self.context['request'].user)
        column_obj = Column.objects.create(
            **validated_data,
        )
        column_obj.admin_users.add(adm_user.id)
        column_obj.save()
        br = Boards.objects.get(id=self.context['request'].data['br_id'])
        br.column.add(column_obj.id)
        br.save()
        return column_obj

